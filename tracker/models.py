from django.db import models
from django.contrib.auth.models import User
from unixtimestampfield import UnixTimeStampField
from django.db.models.signals import post_save, pre_delete, post_delete
from datetime import datetime

# Create your models here.


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    client = models.CharField(max_length=50, blank=True, null=True)
    billable = models.BooleanField(default=False)
    billable_rate = models.DecimalField(
        decimal_places=2, max_digits=10, null=True, blank=True)
    color = models.CharField(max_length=20)


class Tag(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)


class TimeEntry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    start_date = UnixTimeStampField(use_numeric=True, default=0.0)
    end_date = UnixTimeStampField(use_numeric=True, default=0.0)

    class Meta():
        verbose_name_plural = 'Time entries'

    def time_difference(self):
        return self.end_date - self.start_date


class DayEntry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time_total = models.IntegerField(default=0, blank=True)
    time_entries = models.ManyToManyField(TimeEntry)

    class Meta():
        verbose_name_plural = 'Day entries'


def time_entry_save(sender, instance, **kwargs):
    date = datetime.fromtimestamp(instance.start_date)
    day_entry, created = DayEntry.objects.get_or_create(date=date, owner=instance.owner)
    day_entry.time_entries.add(instance)
    day_entry.time_total = 0
    for time_entry in day_entry.time_entries.all():
        day_entry.time_total += time_entry.time_difference()
    day_entry.save()

def time_entry_delete(sender, instance, **kwargs):
    date = datetime.fromtimestamp(instance.start_date)
    day_entry = DayEntry.objects.get(date=date, owner=instance.owner)
    day_entry.time_total = 0
    for time_entry in day_entry.time_entries.all():
        day_entry.time_total += time_entry.time_difference()
    day_entry.save()

def time_entry_post_delete(sender, instance, **kwargs):
    date = datetime.fromtimestamp(instance.start_date)
    day_entry = DayEntry.objects.get(date=date, owner=instance.owner)
    print('count', day_entry.time_entries.count())
    if day_entry.time_entries.count() == 0:
        print('inside')
        day_entry.delete()

post_save.connect(time_entry_save, sender=TimeEntry)
pre_delete.connect(time_entry_delete, sender=TimeEntry)
post_delete.connect(time_entry_post_delete, sender=TimeEntry)