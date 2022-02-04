from django.shortcuts import render
from .serializers import SwiperContentSerializer
from .models import SwiperContent
from rest_framework import viewsets

class SwiperContentView(viewsets.ModelViewSet):
    serializer_class = SwiperContentSerializer
    queryset = SwiperContent.objects.all()