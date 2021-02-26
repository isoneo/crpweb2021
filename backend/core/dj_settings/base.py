"""
Django dj_settings for capybara project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/dj_settings/

For the full list of dj_settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/dj_settings/
"""

from pathlib import Path
import os
import datetime as dt
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# All dj_settings common to all environments
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

MEDIA_URL = '/media/'
# Quick-start development dj_settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%$b@*qn&l_@oekwz*r(yzhj#-9+jngofyoleo(!u^n5dmzggha'

REST_SESSION_LOGIN = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_AUTHENTICATION_METHOD = 'username'
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'




# AUTHENTICATION_BACKENDS = (
#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',
#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
# )


ALLOWED_HOSTS = ['*']


# CORS Settings
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     'http//:localhost:8000','127.0.0.1:8000',
#
# )


# Application definition

BASE_INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simple_history',
]
CUSTOM_INSTALLED_APPS = [

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
    'django.contrib.sites',
    'django_filters',
    'core',
    'user_accounts_app',
    'source_reference_models_app',
    'deal_tracker_app',
    'well_collection_app',
]


INSTALLED_APPS= BASE_INSTALLED_APPS + CUSTOM_INSTALLED_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    # 'django.middleware.gzip.GZipMiddleware',
]

ROOT_URLCONF = 'core.urls'





TEMPLATE_DIRS = [
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

### DB Settings
if os.environ['COMPUTERNAME'] in ['AMDWILLHQ', 'WILLHQ']:
    # POSTGRES_DB_HOST = 'localhost'
    # Proxmox PSQL
    POSTGRES_DB_HOST = '192.168.0.180'
else:
    POSTGRES_DB_HOST = 'SQL'

POSTGRES_DB_user = 'spotfireuser'
POSTGRES_DB_pd = 'password'

DATABASE_ROUTERS = ['dbrouters.DBRouter']


# Rest Framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 40
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ACCESS_TOKEN_LIFETIME': dt.timedelta(minutes=500),
    'REFRESH_TOKEN_LIFETIME': dt.timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
}

### Email Settings
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

# EMAIL_HOST = "GREYHORSE.corp.canaanenergy.com"
# EMAIL_HOST = "mail.canaangas.com"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = "587"
# EMAIL_HOST_USER = "william@crpok.com"
EMAIL_HOST_USER = 'crpwebcontact@gmail.com'
EMAIL_HOST_PASSWORD = 'crpwebdjango111'
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


### File handling
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440000


# AUTH_USER_MODEL = "user_accounts_app.CustomUser"
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': dt.datetime.timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': dt.datetime.timedelta(days=1),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': True,
#     'UPDATE_LAST_LOGIN': True,
#
#     # 'ALGORITHM': 'HS256',
#     # 'SIGNING_KEY': settings.SECRET_KEY,
#     # 'VERIFYING_KEY': None,
#     # 'AUDIENCE': None,
#     # 'ISSUER': None,
#     #
#     # 'AUTH_HEADER_TYPES': ('Bearer',),
#     # 'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     # 'USER_ID_FIELD': 'id',
#     # 'USER_ID_CLAIM': 'user_id',
#     #
#     # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     # 'TOKEN_TYPE_CLAIM': 'token_type',
#     #
#     # 'JTI_CLAIM': 'jti',
#     #
#     # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }