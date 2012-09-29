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
DATABASES = {
    # Point to a local sqlite3 instance by default.
    'default': dj_database_url.config(default='sqlite:///%s' % project_path('db.sqlite'))
}


## Middleware configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


## Installed app configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS += (
    # See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/
    'django.contrib.admin',
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/admindocs/
    'django.contrib.admindocs',

    # django-debug-toolbar
    'debug_toolbar',
)


## Internal IPs configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#internal-ips
INTERNAL_IPS = (
    '127.0.0.1',
)
