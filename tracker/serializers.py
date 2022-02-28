from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DayEntry, Project, TimeEntry
import time

class UserSelrializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['email', 'date_joined', 'last_login']

class TimestampField(serializers.Field):
    def to_representation(self, value):
        value = str(value)
        return time.mktime(time.strptime(value, "%Y-%m-%d"))


class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = Project
        fields = '__all__'


class TimeEntrySerializer(serializers.ModelSerializer):
    
    class Meta():
        model = TimeEntry
        fields = '__all__'

# return day etries list with date in timestamp format
class TimestampDayEntrySerializer(serializers.ModelSerializer):
    timestamp = TimestampField(source='date')
    class Meta():
        model = DayEntry
        fields = ['timestamp', 'time_total']


class DayEntrySerializer(serializers.ModelSerializer):
    class Meta():
        model = DayEntry
        fields = '__all__'

