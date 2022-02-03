from django.db import models
from django.contrib.auth.models import User
from unixtimestampfield import UnixTimeStampField

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    client = models.CharField(max_length=50, blank=True, null=True)
    billable = models.BooleanField(default=False)
    billable_rate = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    color = models.CharField(max_length=20)

class Tag(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

class TimeEntry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True )
    tags = models.ManyToManyField(Tag)
    start_date = UnixTimeStampField(use_numeric=True, default=0.0)
    end_date = UnixTimeStampField(use_numeric=True, default=0.0)

    class Meta():
        verbose_name_plural = 'Time entries'


class DayEntry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    time_entries = models.ManyToManyField(TimeEntry)

    class Meta():
        verbose_name_plural = 'Day entries'