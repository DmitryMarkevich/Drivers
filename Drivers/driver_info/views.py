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
        hours_worked = 0
        delta_time = 0
        for t in queryset:
            if t['status'] == 's':
                delta_time = t['create_date']
            if t['status'] == 'f':
                delta_time = t['create_date'] - delta_time

        hours_worked = delta_time

        # Попытка обработать последнюю запись относительно текущего времени
        # try:
        #     hours_worked = round(hours_worked.total_seconds() / 3600, 2)
        # except AttributeError:
        #     today = datetime.now()
        #     t1 = today - t['create_date']
        #     print(t1)
        #     hours_worked = round(t1.total_seconds() / 3600, 2)

        hours_relax = 0
        for t in queryset:
            if t['status'] == 'f':
                delta_time = t['create_date']
            if t['status'] in ('s', 'o'):
                delta_time = t['create_date'] - delta_time
            hours_relax = delta_time

        hours_off = 0
        for t in queryset:
            if t['status'] == 'o':
                delta_time = t['create_date']
            if t['status'] == 's':
                delta_time = t['create_date'] - delta_time
            hours_off = delta_time

        return Response({'driver_id': driver_id,
                         'hours_worked': round(hours_worked.total_seconds() / 3600, 2),
                         'hours_relax': round(hours_relax.total_seconds() / 3600, 2),
                         'hours_off': round(hours_off.total_seconds() / 3600, 2),
                         })
