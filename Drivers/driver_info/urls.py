from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path('api/v1/driver_info/<int:driver_id>/<int:count_day>/', DriverAPIView.as_view()),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
