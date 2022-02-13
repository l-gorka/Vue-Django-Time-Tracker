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
    print(body)
    try:
        created = User.objects.create(
            username=body['username'], email=body['email'], 
            password=body['password1'])
        return Response('User has been registered', status=202)
    except IntegrityError:
            return Response("User already exists", status=401)
        

@csrf_exempt
@api_view(['GET'])
def ProjectList(request):
    projects = Project.objects.all().order_by('title')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProjectView(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)


@api_view(['POST'])
def ProjectCreate(request):
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
        print('serializer is valid')
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def TimeEntryCreate(request):
    serializer = TimeEntrySerializer(data=request.data)
    if serializer.is_valid():
        print('is valid')
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def TimeEntryList(request):
    entries = TimeEntry.objects.all()
    serializer = TimeEntrySerializer(entries, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def DayEntriesList(request):
    entries = DayEntry.objects.all().order_by('-date')
    serializer = DayEntrySerializer(entries, many=True)
    return Response(serializer.data)
