import json
from datetime import date
from collections import OrderedDict
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
        params = request.query_params
        startdate = date.fromordinal(int(
            params['startdate'])) if 'startdate' in params else date(
            date.today().year, 1, 1)
        enddate = date.fromordinal(int(
            params['enddate'])) if 'enddate' in params else date.today()
        items = int(params['items']) if 'items' in params else 10
        summary_dict = OrderedDict([
            ('max_temp', []),
            ('mean_temp', []),
            ('min_temp', []),
            ('max_dew', []),
            ('mean_dew', []),
            ('min_dew', []),
            ('max_humidity', []),
            ('mean_humidity', []),
            ('min_humidity', []),
            ('max_sea_pressure', []),
            ('mean_sea_pressure', []),
            ('min_sea_pressure', []),
            ('max_visibility', []),
            ('mean_visibility', []),
            ('min_visibility', []),
        ])
        for key in ['temp', 'dew', 'humidity', 'sea_pressure', 'visibility']:
            max_key = 'max_' + key
            mean_key = 'mean_' + key
            min_key = 'min_' + key
            max_ = [getattr(instance, max_key) for instance in WeatherModel.objects.filter(
                    date__gte=startdate, date__lte=enddate).order_by(
                        '-' + max_key)[:items]]
            _ = [getattr(instance, mean_key)
                 for instance in WeatherModel.objects.all()[:items]]
            mean_ = sum(_) / len(_)

            min_ = [getattr(instance, min_key) for instance in WeatherModel.objects.filter(
                    date__gte=startdate, date__lte=enddate).order_by(min_key)[:items]]
            summary_dict['max_' + key] = max_
            summary_dict['mean_' + key] = mean_
            summary_dict['min_' + key] = min_
        # min_temps = WeatherModel.objects.order_by('min_temp')[:10

        # serializer = WeatherSerializer(max_temp, many=True)
        return Response(summary_dict)
