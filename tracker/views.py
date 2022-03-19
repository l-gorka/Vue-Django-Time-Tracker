from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import DayEntry, Project, TimeEntry
from .serializers import (ChangePasswordSerializer, DayEntrySerializer,
                          ProjectSerializer, TimeEntrySerializer,
                          UserCreateSerializer, UserSelrializer)


@api_view(['GET'])
def user_data(request):
    user = User.objects.get(id=request.user.id)
    serializer = UserSelrializer(user)
    return Response(serializer.data)


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            serializer = UserCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except IntegrityError:
            return Response('Username already taken', 400)
        except Exception as e:
            return Response('Password incorrect', 400)
        return Response('Created', 201)


@api_view(['POST'])
def password_change(request):
    user = User.objects.get(id=request.user.id)
    serializer = ChangePasswordSerializer(data=request.data)
    if serializer.is_valid():
        check = user.check_password(
            serializer.validated_data.get("old_password"))
        if check:
            user.set_password(serializer.validated_data.get("password"))
            user.save()
            return Response('Password changed', 200)
        else:
            return Response('Password you entered is incorrect. Please retype your current password.', status=401)
    else:
        return Response("Password can't be a commonly used password or similar to your other personal information.", 400)


@api_view(['GET'])
def project_list(request):
    projects = Project.objects.filter(owner=request.user).order_by('title')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def project_create(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Invalid data", 402)


@api_view(['POST'])
def project_update(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Invalid data", 402)


@api_view(['POST'])
def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    if request.user == project.owner:
        project.delete()
        return Response('Item has been deleted', status=202)
    else:
        return Response('Forbidden', 403)


@api_view(['POST'])
def TimeEntryUpdate(request, pk):
    entry = TimeEntry.objects.get(id=pk)
    serializer = TimeEntrySerializer(instance=entry, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def time_entry_create(request):
    serializer = TimeEntrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def time_entry_list(request):
    entries = TimeEntry.objects.filter(
        owner=request.user).order_by('start_date')
    serializer = TimeEntrySerializer(entries, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def time_entry_delete(request, pk):

    entry = TimeEntry.objects.get(id=pk)
    if request.user == entry.owner:
        entry.delete()
        return Response('Item has been deleted', status=202)
    else:
        return Response('Forbidden', 403)


@api_view(['GET'])
def day_entries_list(request):
    entries = DayEntry.objects.filter(owner=request.user).order_by('-date')
    serializer = DayEntrySerializer(entries, many=True)
    return Response(serializer.data)
