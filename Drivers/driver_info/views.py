from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DriverLog


# from .serializers import DriverSerializer


# Create your views here.


class DriverAPIView(APIView):
    def get(self, request, driver_id):
        queryset = DriverLog.objects.values('create_date', 'driver_id', 'status').filter(driver_id=driver_id)
        delta_time = None
        data = {}
        for stat in ('s', 'f', 'o'):
            for q in queryset:
                if q['status'] == stat:
                    delta_time = q['create_date']
                elif q['status'] != stat and delta_time != None:
                    delta_time = q['create_date'] - delta_time
                    round_time = round(delta_time.total_seconds() / 3600, 2)
                    try:
                        data[stat] += round_time
                    except KeyError:
                        data[stat] = round_time
                    delta_time = None

        return Response({'driver_id': driver_id, **data})
