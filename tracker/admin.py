from re import T
from django.contrib import admin
from .models import Project, DayEntry, TimeEntry, Tag
# Register your models here.

admin.site.register(Project)
admin.site.register(DayEntry)
admin.site.register(TimeEntry)
admin.site.register(Tag)