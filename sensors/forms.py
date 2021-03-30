from django import forms
from .models import Sensor

class SensorForm(forms.ModelForm):
    sensor_name = forms.CharField(label='Sensor Name', max_length=100)
    class Meta:
        model = Sensor
        fields = ("sensor_name",)
