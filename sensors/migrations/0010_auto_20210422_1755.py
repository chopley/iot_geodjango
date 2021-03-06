# Generated by Django 3.2 on 2021-04-22 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0009_rename_imei_sensordata_imei_sensor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='sensor',
        ),
        migrations.AlterField(
            model_name='sensor',
            name='imei',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='imei_sensor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sensors.sensor', to_field='imei'),
            preserve_default=False,
        ),
    ]
