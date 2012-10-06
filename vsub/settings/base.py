"""Base settings available to all environments."""

# Based on https://github.com/rdegges/django-skel and
# https://github.com/cyberdelia/django-heroku-template.

import os
import sys
from django.contrib.messages import constants as messages

## Path configuration
# Absolute path to our site directory.
# NOTE: Use dirname() twice as the settings file is two levels deep.
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create an absolute path from a path relative to the site root.
site_path = lambda path: os.path.normpath(os.path.join(SITE_ROOT, path))

# Name of the site.
SITE_NAME = os.path.basename(SITE_ROOT)

# Absolute path to our project directory.
PROJECT_ROOT = os.path.dirname(SITE_ROOT)

# Create an absolute path from a path relative to the project root.
project_path = lambda path: os.path.normpath(os.path.join(PROJECT_ROOT, path))

# Add our site root to the pythonpath so that we can refer to project
# modules without having to use the project's name.
sys.path.append(SITE_ROOT)


## Debug configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG


## Admin and manager configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Marcus R. Brown', 'mrbrown@precision-mojo.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS


## Timezone and localization configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/Phoenix'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True


## Media configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = site_path('media/')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'


## Static files configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# NOTE: We place this path at the our *site* root, not the project root. This
# allows us to run collectstatic during development without worrying about
# overwriting static files in app-relative static/ directories.
STATIC_ROOT = project_path('static_collected/')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-dirs
STATICFILES_DIRS = ()

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-storage
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'


## Secret key configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = '4=py*2g1gl=cgjqcb4v*gr^&amp;5nxt2@d%b+!#l(2eeb#sa_0yxq'


## Template configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    site_path('templates/')
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
# NOTE: All except the last are defaults.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    '%s.context_processors.analytical_domain' % SITE_NAME,
)


## Middleware configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # TODO: Disable GZIP middleware until we have a clean way of ensuring that
    # it's first in the list.
    #'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


## URL configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME


## WSGI configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME


## Cache configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'staticfiles': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(PROJECT_ROOT, 'static_cache'),
        'TIMEOUT': 100 * 365 * 24 * 60 * 60,
        'OPTIONS': {
            'MAX_ENTRIES': 100 * 1000
        },
    },
}


## Installed app configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/humanize/
    'django.contrib.humanize',

    # Third-party apps
    # django-pipeline
    'pipeline',
    # django-analytical,
    'analytical',
    # South
    'south',
    # django-robots
    'robots',

    # Project libraries
    '%s' % SITE_NAME,
    'libs.bootstrap',
)


## Logging configuration
# NOTE: Don't filter HTTP 500 error emails in not DEBUG environments (the
# default configuration does this).
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


## Messages configuration
# See: https://docs.djangoproject.com/en/dev/ref/contrib/messages/#message-tags
# Setup tags to use Twitter Bootstrap alert styles (from
# https://github.com/estebistec/bootstrap-pipelined)
MESSAGE_TAGS = {
    messages.DEBUG: '',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: '',
    messages.ERROR: 'alert-error',
}


## django-pipeline configuration
# See: http://django-pipeline.readthedocs.org/en/latest/configuration.html
# TODO: This uses a workaround for PipelineFinderStorage for running on
# Windows.
PIPELINE_STORAGE = '%s.settings.pipeline_helpers.PipelineFinderStorageCorrected' % SITE_NAME

# See: http://django-pipeline.readthedocs.org/en/latest/configuration.html#specifying-files
PIPELINE_CSS = {
    'standard': {
        'source_filenames': (
            # TODO: Use the checked-in .css until django-pipeline places
            # compiled output into the STATIC_ROOT directory.
            #'less/bootstrap.less',
            'css/bootstrap.css',
        ),
        'output_filename': 'css/s.min.css',
    },
    'responsive': {
        'source_filenames': (
            # TODO: Use the checked-in .css until django-pipeline places
            # compiled output into the STATIC_ROOT directory.
            #'less/responsive.less',
            'css/bootstrap-responsive.css',
        ),
        'output_filename': 'css/r.min.css',
    },
}

PIPELINE_JS = {
    'standard': {
        'source_filenames': (
            'js/bootstrap-affix.js'
            'js/bootstrap-alert.js',
            'js/bootstrap-button.js',
            'js/bootstrap-carousel.js',
            'js/bootstrap-collapse.js',
            'js/bootstrap-dropdown.js',
            'js/bootstrap-modal.js',
            'js/bootstrap-scrollspy.js',
            'js/bootstrap-tab.js',
            'js/bootstrap-tooltip.js',
            'js/bootstrap-popover.js',
            'js/bootstrap-transition.js',
            'js/bootstrap-typeahead.js',
        ),
        'output_filename': 'js/s.min.js',
    }
}

# See: http://django-pipeline.readthedocs.org/en/latest/configuration.html#pipeline-css-compressor
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CssminCompressor'

# See: http://django-pipeline.readthedocs.org/en/latest/configuration.html#pipeline-js-compressor
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'

# See: http://django-pipeline.readthedocs.org/en/latest/compilers.html#compilers
PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)
# TODO: Strip off the /usr/bin/env portion of the value provided by
# django-pipeline if env isn't on the path.
#PIPELINE_LESS_BINARY = 'lessc'


## django-htmlmin configuration
# See: http://pypi.python.org/pypi/django-htmlmin
# TODO: Disable HTML minifying because it breaks the IE-specific code at the
# top of base.html.
HTML_MINIFY = False
KEEP_COMMENTS_ON_MINIFYING = True


## django-analytical configuration
# See: http://packages.python.org/django-analytical/services/google_analytics.html
GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get('GOOGLE_ANALYTICS_TRACKING_ID', '')
GOOGLE_ANALYTICS_TRACKING_STYLE = 3  # google_analytics.TRACK_MULTIPLE_DOMAINS'

# See: http://packages.python.org/django-analytical/services/gauges.html
GAUGES_SITE_ID = os.environ.get('GAUGES_SITE_ID', '')

# See: http://packages.python.org/django-analytical/services/mixpanel.html
MIXPANEL_API_TOKEN = os.environ.get('MIXPANEL_API_TOKEN', '')
