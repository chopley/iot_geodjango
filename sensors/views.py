from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.views.generic import DetailView, ListView
from .models import Sensor, SensorData
from django.http import HttpResponse



class SensorDetailView(ListView):
    """
        Sensor detail view.
    """
    template_name = 'sensors/sensor.html'
    #model = SensorData
    queryset = SensorData.objects.filter(location__isnull=False)


