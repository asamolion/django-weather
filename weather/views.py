import json
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .models import WeatherModel
from .serializers import WeatherSerializer


class WeatherViewSet(viewsets.ModelViewSet):
    '''
    API endpoint viewset for WeatherModel class
    '''
    queryset = WeatherModel.objects.all()
    serializer_class = WeatherSerializer


class WeatherSummaryView(APIView):
    '''
    gives summary of the weather data
    '''
    def get(self, request, format=None):
        weather = WeatherModel.objects.all()
        serializer = WeatherSerializer(weather)
        summary_dict = {
            'mean_temp': 100,
            'max_temp': 1000,
        }
        return Response(summary_dict)