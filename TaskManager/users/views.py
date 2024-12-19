from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class UserViewset(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
