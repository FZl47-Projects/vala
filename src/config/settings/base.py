"""
    Django Version => 4.2.6
"""
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-yb@%1c&455k_g&y7w%+x13$vb*r24wo@=chrzp%5^aa5wd#%7&')

DEBUG = os.getenv('DEBUG', True)

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', 'http://127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps
    'apps.core',
    'apps.public',
    'apps.account',
    'apps.dashboard',
    'apps.notification',

    # Third Party Apps
    'django_cleanup.apps.CleanupConfig',
    'django_render_partial',
    'django_q',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'custom_tags': 'apps.core.templatetags.custom_tags'
            }
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

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

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = False

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / os.getenv('STATIC_ROOT', 'static')

STATICFILES_DIRS = [
    BASE_DIR / 'static/assets'
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / os.getenv('MEDIA_ROOT', 'static/media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.User'  # custom user model
LOGIN_URL = '/u/login'

Q_CLUSTER = {
    'name': 'django-q',
    'timeout': 60,
    'orm':'default'
    # 'redis': {
    #     'host': 'localhost',
    #     'port': 6379,
    #     'db': 0,
    #     'socket_timeout': None,
    #     'charset': 'utf-8',
    #     'errors': 'strict',
    # }
}

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

REDIS_CONFIG = {
    'HOST': 'localhost',
    'PORT': '6379'
}

RESET_PASSWORD_CONFIG = {
    'TIMEOUT': 60,  # by sec
    'CODE_LENGTH': 6,
    'STORE_BY': 'reset_password_phonenumber_{}'
}

CONFIRM_PHONENUMBER_CONFIG = {
    'TIMEOUT': 60,  # by sec
    'CODE_LENGTH': 6,
    'STORE_BY': 'confirm_phonenumber_{}'
}

SMS_CONFIG = {
    'API_KEY': os.environ.get('SMS_API_KEY'),
    'API_URL': 'http://rest.ippanel.com/v1/messages/patterns/send',
    'ORIGINATOR': '983000505'
}