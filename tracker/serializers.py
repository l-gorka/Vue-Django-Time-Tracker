from rest_framework import serializers
from .models import DayEntry, Project, TimeEntry
from datetime import timezone

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return value.timestamp()


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


