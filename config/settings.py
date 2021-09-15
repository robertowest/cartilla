import os
from config.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, 'templates'),]

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Tucuman'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

MEDIA_URL  = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

INSTALLED_APPS += [
    'cartilla',
]
