from rest_framework import serializers
from .models import Project, TimeEntry


class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = Project
        fields = '__all__'


class TimeEntrySerializer(serializers.ModelSerializer):
    
    class Meta():
        model = TimeEntry
        fields = '__all__'

