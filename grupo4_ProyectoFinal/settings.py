"""
Django settings for grupo4_ProyectoFinal project.
"""

from pathlib import Path
import os 
# ----------------------------------------------------------------------
# [MODIFICACIÓN 1] - Importamos 'config' de python-decouple
from decouple import config 
# ----------------------------------------------------------------------

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!

# ----------------------------------------------------------------------
# [MODIFICACIÓN 2] - Leemos la SECRET_KEY de la variable de entorno
SECRET_KEY = config('SECRET_KEY')
# ----------------------------------------------------------------------

# SECURITY WARNING: don't run with debug turned on in production!
# ----------------------------------------------------------------------
# [MODIFICACIÓN 3] - Leemos DEBUG del archivo .env (default=False en producción)
DEBUG = config('DEBUG', default=False, cast=bool)

# [MODIFICACIÓN 4] - Leemos ALLOWED_HOSTS del archivo .env
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost').split(',')
# ----------------------------------------------------------------------


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.autenticacion.apps.AutenticacionConfig', 
    'apps.articulos.apps.ArticulosConfig',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ----------------------------------------------------------------------
    # [MODIFICACIÓN 5] - Añadimos WhiteNoise para servir archivos estáticos eficientemente
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ----------------------------------------------------------------------
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'grupo4_ProyectoFinal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'grupo4_ProyectoFinal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', 
    }
}

# ----------------------------------------------------------------------
# [MODIFICACIÓN 6] - Configuración de Base de Datos para Producción (PostgreSQL)
# Leemos la configuración de la base de datos desde la URL que nos da el hosting (Render, Railway)
import dj_database_url

DATABASES['default'] = dj_database_url.config(
    # Si la variable DATABASE_URL existe en el hosting, la usa.
    # Si no existe (estamos en local), usa la configuración SQLite de arriba.
    default=config('DATABASE_URL', default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"),
    conn_max_age=600
)
# ----------------------------------------------------------------------


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'es-AR' 
TIME_ZONE = 'America/Argentina/Buenos_Aires' 

USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = (BASE_DIR / 'static',)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'autenticacion.Usuario'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# ----------------------------------------------------------------------
# [MODIFICACIÓN 7] - Configuración de WhiteNoise (Almacenamiento de Estáticos)
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}
# ----------------------------------------------------------------------