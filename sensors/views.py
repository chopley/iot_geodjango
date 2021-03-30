from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.views.generic import DetailView, ListView
from .models import Sensor, SensorData
from django.http import HttpResponse
from .forms import SensorForm
from django.views.generic.edit import FormMixin
from django.views.generic.edit import ModelFormMixin



class SensorListView(ListView):
    """
        Sensor detail view.
    """
    template_name = 'sensors/sensor.html'
    model = SensorData


    def get_queryset(self):
        if(self.request.method == 'GET'):
            data  = SensorData.objects.filter(sensor__name="Woodbury", location__isnull=False)
        else:
            data =  SensorData.objects.filter(sensor__name=self.request.POST['sensor_name'], location__isnull=False)
        print(data.first())
        return data

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SensorForm()
        return context




