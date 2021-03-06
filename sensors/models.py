from django.contrib.gis.db import models
from datetime import datetime


class Sensor(models.Model):
    """
    Represents a Sensor
    """
    name = models.CharField(max_length=200, null=True, blank=True)
    imei = models.CharField(max_length=15, unique=True)
    frequency = models.IntegerField()


class SensorData(models.Model):
    """
    Represents a single Sensor datapoint
    """
    imei_sensor = models.ForeignKey(Sensor, to_field='imei', on_delete=models.CASCADE,)
    date = models.DateTimeField(default=datetime.now)
    sensor_gps_time = models.CharField(max_length=30)
    sensor_data = models.FloatField()
    location = models.PointField()
    battery_voltage_main = models.FloatField()
    battery_voltage_secondary = models.FloatField()
    temperature = models.FloatField()

    @property
    def lat_lng(self):
        return list(getattr(self.location, 'coords', [])[::-1])

    @property
    def sensor_data_val(self):
        return list(getattr(self.sensor_data, 'coords', [])[::-1])


