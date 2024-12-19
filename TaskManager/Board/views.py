from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Board, Task
from .serializers import BoardSerializer, TaskSerializer

class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



