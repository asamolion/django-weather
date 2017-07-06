import json
from datetime import date
from django.utils.dateformat import DateFormat
from collections import OrderedDict
from django.shortcuts import render
from rest_framework import viewsets, mixins, status
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
        response_dict = {}
        params = request.query_params
        startdate = date.fromordinal(int(
            params['startdate'])) if 'startdate' in params else date(
            date.today().year, 1, 1)
        enddate = date.fromordinal(int(
            params['enddate'])) if 'enddate' in params else date.today()
        items = int(params['items']) if 'items' in params else 10

        summary_dict = {}
        # summary_dict['start_date'] = DateFormat(date.fromordinal(startdate)).format('Y-m-d')
        # summary_dict['end_date'] = DateFormat(date.fromordinal(enddate)).format('Y-m-d')
        # summary_dict['items'] = items
        param_dict = OrderedDict([
            ('start_date', DateFormat(startdate).format('Y-m-d')),
            ('end_date', DateFormat(enddate).format('Y-m-d')),
            ('items', items),
        ])
        if items == 0:
            response_dict['status'] = True,
            response_dict['error'] = 'No Content',
            response_dict['params'] = param_dict
            response_dict['summary'] = summary_dict
            return Response(response_dict, status=status.HTTP_204_NO_CONTENT)

        for key in ['temp', 'dew', 'humidity', 'sea_pressure', 'visibility']:
            max_key = 'max_' + key
            mean_key = 'mean_' + key
            min_key = 'min_' + key
            max_ = [getattr(instance, max_key) for instance in WeatherModel.objects.filter(
                    date__gte=startdate, date__lt=enddate).order_by(
                        '-' + max_key)[:items]]
            mean_list = [getattr(instance, mean_key)
                         for instance in WeatherModel.objects.all()[:items]]
            mean_ = sum(mean_list) / len(mean_list)

            min_ = [getattr(instance, min_key) for instance in WeatherModel.objects.filter(
                    date__gte=startdate, date__lte=enddate).order_by(min_key)[:items]]
            summary_dict[max_key] = max_
            summary_dict[mean_key] = mean_
            summary_dict[min_key] = min_

        response_dict['summary'] = summary_dict
        response_dict['status'] = True,
        response_dict['error'] = '',
        response_dict['params'] = param_dict
        response_dict['summary'] = summary_dict
        return Response(response_dict, status=status.HTTP_200_OK)
