"""Settings used in the production environment."""

from memcacheify import memcacheify
from postgresify import postgresify

from base import *


## Email configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER


## Database configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = postgresify()


## Cache configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = memcacheify()


## Secret key configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Use the value set in the Heroku configuration.
SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
