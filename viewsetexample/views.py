from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from viewsetexample.models import University
from viewsetexample.serializer import UniversitySerializer


class UniversityView(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
