from django.shortcuts import render
from rest_framework import generics
from .models import Teacher
from api.serializers import TeacherSerializer

# Create your views here.
class TeachersList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'pk'