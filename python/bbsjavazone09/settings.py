import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
   ('Steingrim', 'std@bbs.no'),
)

MANAGERS = ADMINS

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sessions',

    'development_utils',
    'darts',
)

STATIC_ROOT = 'media'

ROOT_URLCONF = 'bbsjavazone09.urls'

TEMPLATE_DIRS = (
    os.getenv('DJANGO_TEMPLATE_PATH'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'bbsjavazone09.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'Europe/Oslo'
LANGUAGE = 'no'
LANGUAGE_CODE = 'no'
SITE_ID = 1
USE_I18N = True

MEDIA_ROOT = os.getenv('DJANGO_MEDIA_ROOT')
MEDIA_URL = 'http://localhost:8080/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 'gnq)o%6=31yv@*v(jndoj-$*4y_@5j0&pta=@frf=s_5%rh(ze'
