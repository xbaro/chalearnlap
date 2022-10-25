"""
Django settings for chalearnweb project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import typing
from pathlib import Path
import sentry_sdk

from django.contrib.messages import constants as message_constants
from sentry_sdk.integrations.django import DjangoIntegration

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False) in [True, 'True', 'true', '1', 1]

CHALEARNLAP_VERSION = os.environ.get('CHALEARNLAP_VERSION', '2.1.0')

if os.environ.get('SENTRY_DSN', None) is not None:
    sentry_sdk.init(
        dsn=os.environ.get('SENTRY_DSN'),
        release=os.environ.get('SENTRY_RELEASE', CHALEARNLAP_VERSION),
        environment=os.environ.get('SENTRY_ENV', 'Production'),
        integrations=[DjangoIntegration()],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,

        max_breadcrumbs=50,
        debug=DEBUG,
        server_name=os.getenv('SENTRY_SERVER_NAME'),
        attach_stacktrace=True,
    )

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent

# GET SECRETS PATH
SECRETS_PATH = os.environ.get('SECRETS_PATH', '/run/secrets')


def _read_secret(key: str,
                 default: typing.Optional[typing.Any] = None,
                 secret_path: typing.Optional[str] = None):
    """
        Read configuration parameter from secrets and/or environment variable
        :param key: Key to find for
        :param default: Default value in case the key is not found
        :param secret_path: Custom secrets' path
        :return: The value for the key configuration value
    """
    # If secret path is not provided, use default
    if secret_path is None:
        secret_path = SECRETS_PATH

    # Check environment variables
    value = os.getenv(key, None)
    if value is not None:
        return value
    # Check file environment variable
    file_path = os.getenv('{}_FILE'.format(key.upper()), None)
    if file_path is None:
        file_path = os.path.join(secret_path, key.upper())
    if file_path is not None and os.path.exists(file_path):
        with open(file_path, 'r') as secret:
            value = secret.read()
    if value is None:
        value = default
    return value


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _read_secret('SECRET_KEY')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
DIRECTORY = getattr(sentry_sdk, 'FILEBROWSER_DIRECTORY', '')

# Application definition
INSTALLED_APPS = [
    'django.contrib.sites',
    'registration', #should be immediately above 'django.contrib.admin'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'datetimewidget',
    'watson',
    'jfu',
    'sorl.thumbnail',
    'django_extensions',
    'chalearnlap.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chalearnlap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processors.base_context',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'chalearnlap.wsgi.application'
ASGI_APPLICATION = 'chalearnlap.asgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DB_NAME = os.environ.get('DB_NAME', 'chalearn')
if os.environ.get('DB_ENGINE', 'mysql') == 'sqlite3':
    DB_NAME = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), DB_NAME + '.sqlite3')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{}'.format(os.environ.get('DB_ENGINE', 'mysql')),
        'NAME': DB_NAME,
        'USER': os.environ.get('DB_USER', 'chalearn'),
        'PASSWORD': _read_secret('DB_PASSWORD', 'chalearn'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', 3306),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Override messages to feedback information
MESSAGE_TAGS = {
    message_constants.DEBUG: 'debug',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}

# Registration settings
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_EMAIL_HTML = False
SITE_ID = os.environ.get('SITE_ID', 1)

# GMAIL SMTP settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None),
EMAIL_HOST_PASSWORD = _read_secret('EMAIL_HOST_PASSWORD', None),
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', None),
DEFAULT_TO_EMAIL = ''

# Use console as email backend on debug except if SMTP password is given
if DEBUG and (EMAIL_HOST_PASSWORD is None or os.environ.get('EMAIL_CONSOLE', False) in [True, 'true', 'True', '1', 1]):
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = '/'

# CKEditor settings

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': '400px',
        'width': 'auto',
    },
}

CKEDITOR_UPLOAD_PATH = "ck_uploads"

# Account Verification (none or optional)
ACCOUNT_EMAIL_VERIFICATION = 'optional'