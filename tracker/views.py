from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt

import json

from .models import DayEntry, Project, TimeEntry
from .serializers import DayEntrySerializer, ProjectSerializer, TimeEntrySerializer
# Create your views here.


@api_view(['POST'])
def register_user(request):
    body = json.loads(request.body)
    try:
        created = User.objects.create(
            username=body['username'], email=body['email'], 
            password=body['password1'])
        return Response('User has been registered', status=202)
    except IntegrityError:
            return Response("User already exists", status=401)
        

@csrf_exempt
@api_view(['GET'])
def project_list(request):
    projects = Project.objects.filter(owner=request.user).order_by('title')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProjectView(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)


@api_view(['POST'])
def project_create(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def TimeEntryView(request, pk):
    entry = TimeEntry.objects.get(id=pk)
    serializer = TimeEntrySerializer(entry)
    return Response(serializer.data)


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
    entries = TimeEntry.objects.filter(owner=request.user)
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
    print(entries[0].date)
    serializer = DayEntrySerializer(entries, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def day_entries_chart_list(request):
    pass