# Generated by Django 3.1.7 on 2021-04-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0003_auto_20210409_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='sensor_gps_time',
            field=models.CharField(max_length=30),
        ),
    ]
