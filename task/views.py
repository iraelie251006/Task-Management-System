from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserProfileSerializer
from rest_framework.response import Response

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]