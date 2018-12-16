"""
Contains example of custom local settings.
"""

import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Your too secret key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'diploma',
        'USER': 'beph',
        'PASSWORD': 'bephpass',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'clustering': {
        'NAME': 'trained_model',
        'ENGINE': 'djongo',
    }
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL = '/static/'
STATIC_ROOT = None
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
