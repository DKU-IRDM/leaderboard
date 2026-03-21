import os

import dj_database_url

from pathlib import Path

from dotenv import load_dotenv


# env
load_dotenv()

# path
BASE_DIR = Path(__file__).resolve().parent.parent

# secret
SECRET_KEY = os.getenv('SECRET_KEY', 'django_secret_key')
APP_PASSWORD = os.getenv('APP_PASSWORD', 'app_password')
WEB_PASSWORD = os.getenv('WEB_PASSWORD', 'web_password')
DEBUG = bool(int(os.getenv('DEBUG', '0')))

# host
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.vercel.app',
]

# app
ROOT_URLCONF = 'api.urls'
WSGI_APPLICATION = 'api.wsgi.app'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'web',
    'import_export',
]

# cors
CORS_ALLOW_ALL_ORIGINS = True

# middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# template
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

# db
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL),
}

# password
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# i18n
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True

# static
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
