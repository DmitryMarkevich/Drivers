from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from datetime import datetime
import pytz

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DriverLog


# from .serializers import DriverSerializer


# Create your views here.


class DriverAPIView(APIView):
    def get(self, request, driver_id):
        queryset = list(DriverLog.objects.values('create_date', 'driver_id', 'status').filter(driver_id=driver_id))
        id = driver_id
        data = {}
        for state, t in zip(('s', 'f', 'o'), ('working_hours', 'time_relax', 'time_off')):
            data[t] = round(sum([(queryset[(queryset.index(q) + 1)]['create_date'] - q['create_date']).total_seconds()
                                 if queryset.index(q) < len(queryset) - 1 else (
                    datetime.now(pytz.utc) - q['create_date']).total_seconds()
                                 for q in queryset if q['status'] == state]) / 3600, 2)

        return Response({'driver_id': driver_id, **data, })
