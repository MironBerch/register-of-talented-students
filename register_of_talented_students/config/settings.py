from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-8fajd3)on9ecoq&&8__eryh-d5sz@6!8ky3+y0u5k6gw8!q$^t'
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'reporting',
    'core',
    'students',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_auto_logout.middleware.auto_logout',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django_auto_logout.context_processors.auto_logout_client',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / 'static']
else:
    STATIC_ROOT = BASE_DIR / 'static'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.User'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


LOGIN_URL = '/signin'
LOGIN_REDIRECT_URL = 'list'


AUTO_LOGOUT = {
    'IDLE_TIME': 300,
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
    'MESSAGE': 'Вы бездействовали более 5 минут. Пожалуйста, войдите снова, чтобы продолжить.',
}