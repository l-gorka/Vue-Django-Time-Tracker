
import time

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import DayEntry, Project, TimeEntry


class UserSelrializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['email', 'date_joined', 'last_login']


class UserCreateSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True, validators=[validate_password])

    class Meta():
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user


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


class TimestampDayEntrySerializer(serializers.ModelSerializer):
    timestamp = TimestampField(source='date')

    class Meta():
        model = DayEntry
        fields = ['timestamp', 'time_total']


class DayEntrySerializer(serializers.ModelSerializer):
    class Meta():
        model = DayEntry
        fields = '__all__'


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')
