"""Settings used in the development environment."""

import dj_database_url

from base import *

## Debug configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG


## Email configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


## Database configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASE = {
    # Point to a local sqlite3 instance by default.
    'default': dj_database_url.config(default='sqlite3:///%s'
        % project_path('db.sqlite'))
}


## Cache configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
