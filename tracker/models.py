from django.db import models
from django.contrib.auth.models import User
from unixtimestampfield import UnixTimeStampField
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
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

    def __str__(self):
        return str(datetime.fromtimestamp(self.start_date))


class DayEntry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time_total = models.IntegerField(default=0, blank=True)
    time_entries = models.ManyToManyField(TimeEntry)

    class Meta():
        verbose_name_plural = 'Day entries'

    def __str__(self):
        return str(self.date)

    def get_time_total(self):
        self.time_total = 0
        for time_entry in self.time_entries.all():
            self.time_total += time_entry.time_difference()
        print(self.date, self.time_total)



def time_entry_save(sender, instance, **kwargs):
    # add time entry to day entry, if not present, create new day entry
    date = datetime.fromtimestamp(instance.start_date)
    day_entry, created = DayEntry.objects.get_or_create(
        date=date, owner=instance.owner)
    day_entry.time_entries.add(instance)
    # calculate total day time based on time entries
    day_entry.get_time_total()
    day_entry.save()


def time_entry_pre_save(sender, instance, **kwargs):
    # in case of changing time entry date, first it needs to be removed from corresponding day entry
    try:
        day_entry = DayEntry.objects.get(time_entries=instance.id)
    except DayEntry.DoesNotExist:
        day_entry = None
    if day_entry:
        day_entry.time_entries.remove(instance)
        if day_entry.time_entries.count() == 0:
            day_entry.delete()
        else:
            day_entry.get_time_total()
            day_entry.save()
    

    


def time_entry_delete(sender, instance, **kwargs):
    # in case of delting time entry, calculate total time of coresponding day entry again
    date = datetime.fromtimestamp(instance.start_date)
    day_entry = DayEntry.objects.get(date=date, owner=instance.owner)
    day_entry.get_time_total()
    day_entry.save()


def time_entry_post_delete(sender, instance, **kwargs):
    # in case of deleting time entry check if there are other time entries at that day
    # if no, delete day entry
    date = datetime.fromtimestamp(instance.start_date)
    day_entry = DayEntry.objects.get(date=date, owner=instance.owner)
    print('pd', day_entry)
    if day_entry.time_entries.count() == 0:
        day_entry.delete()


pre_save.connect(time_entry_pre_save, sender=TimeEntry)
post_save.connect(time_entry_save, sender=TimeEntry)
pre_delete.connect(time_entry_delete, sender=TimeEntry)
post_delete.connect(time_entry_post_delete, sender=TimeEntry)
