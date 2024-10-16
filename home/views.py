from django.shortcuts import render, redirect
from .models import *  # Import all models

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

@api_view(['GET'])
def apiOverview(request):
    # Define available API endpoints
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/create-task/',
        'Update': '/update-task/<str:pk>/',
        'Delete': '/delete-task/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def TaskList(request):
    tasks = ToDo.objects.all()  # Fetch all tasks
    serializer = TaskSerializer(tasks, many=True)  # Serialize task data
    return Response(serializer.data)

@api_view(['GET'])
def TaskDetail(request, pk):
    tasks = ToDo.objects.get(id=pk)  # Fetch task by ID
    serializer = TaskSerializer(tasks, many=False)  # Serialize task data
    return Response(serializer.data)

@api_view(['POST'])
def UpdateTask(request, pk):
    task = ToDo.objects.get(id=pk)  # Fetch task to update
    serializer = TaskSerializer(instance=task, data=request.data)  # Create serializer instance
    if serializer.is_valid():  # Validate data
        serializer.save()  # Save updated task
    return Response(serializer.data)

@api_view(['POST'])
def CreateTask(request):
    serializer = TaskSerializer(data=request.data)  # Create serializer instance
    if serializer.is_valid():  # Validate data
        serializer.save()  # Save new task
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteTask(request, pk):
    task = ToDo.objects.get(id=pk)  # Fetch task to delete
    task.delete()  # Delete the task
    return Response("Task deleted successfully.")  # Return success message
