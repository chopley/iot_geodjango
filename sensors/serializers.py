from django.contrib.auth.models import User, Group
from rest_framework import serializers
from sensors.models import SensorData, Sensor


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name','imei','frequency']

class SensorSerializerImei(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ['imei']

class SensorDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorData
        fields = ['sensor', 'imei','date', 'sensor_gps_time','temperature','sensor_data','location','battery_voltage_main','battery_voltage_secondary']


