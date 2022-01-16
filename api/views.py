from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def home(request):
    api_urls = {
        'list': '/todo/all',
        'detail': '/todo/<str:pk>/',
        'create': '/todo',
        'update': '/todo',
        'delete': '/todo',
    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def todo_detail(request, id):
    todos = Todo.objects.get(id=id)
    serializer = TodoSerializer(todos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def todo_create(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes((permissions.AllowAny,))
def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    serializer = TodoSerializer(instance=todo, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return Response('Item deleted!')