from dataclasses import field
from multiprocessing import set_forkserver_preload
from rest_framework import serializers
from .models import DayEntry, Project, TimeEntry


class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = Project
        fields = '__all__'


class TimeEntrySerializer(serializers.ModelSerializer):
    
    class Meta():
        model = TimeEntry
        fields = '__all__'


class DayEntrySerializer(serializers.ModelSerializer):

    class Meta():
        model = DayEntry
        fields = '__all__'