from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Student
from .serializers import (
    StudentSerializer,
    RegisterSerializer,
    
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User


# Create student view
class StudentView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)
    queryset = Student.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# student detail view.
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)
    lookup_url_kwarg = "id"
    queryset = Student.objects.all()


# User register view
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            register = serializer.save()
            serializer = RegisterSerializer(register)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


