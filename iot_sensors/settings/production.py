"""
Django settings for iot_sensors project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from .base import *
from pathlib import Path
import django_heroku
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#for heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

from os import environ

GEOS_LIBRARY_PATH = environ.get('GEOS_LIBRARY_PATH')
GDAL_LIBRARY_PATH = environ.get('GDAL_LIBRARY_PATH')

# Application definition

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

import dj_database_url
django_heroku.settings(locals())
DATABASES = { 'default': dj_database_url.config(conn_max_age=500) }
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


