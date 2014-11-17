"""
Django settings for ccademo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.join(BASE_DIR, "ccademo3")
# print BASE_DIR
TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
)

# Datatel output will be placed here
IMPORTER_DATA_DIR = os.path.join(BASE_DIR, 'data/enroldata')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'abc123'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    '.cca.edu',  # Allow domain and subdomains
]


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'localflavor',

    # 3rd party apps
    'django_countries',
    'simplejson',
    'django_extensions',
    'bootstrapform',
    'widget_tweaks',
    # 'anonymizer',
    'django_messages',
    'todo',
    'stronghold',
    'tinymce',
    'mce_filebrowser',
    'easy_thumbnails',
    'rest_framework',


    # Our apps
    'base',
    'dashboard',
    'people',
    'courses',
    'scheduler',
    'notifications',
    'pages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'stronghold.middleware.LoginRequiredMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django_messages.context_processors.inbox"
)

# Stronghold makes whole site login-required except for exemptions
STRONGHOLD_DEFAULTS = True
STRONGHOLD_PUBLIC_URLS = ('/','/admin',)


TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace,image",
    'theme': "modern",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'file_browser_callback': 'mce_filebrowser',
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = False
# TINYMCE_FILEBROWSER=True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
)

SITE_ID = 1

# AUTH_USER_MODEL = 'auth.User'

# Via https://pypi.python.org/pypi/django-cas-ng/3.1.0
CAS_SERVER_URL = 'https://cas.cca.edu/cas/login'
CAS_ADMIN_PREFIX = '/admin'
CAS_LOGOUT_COMPLETELY = True

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

# Locations for static files
STATICFILES_DIRS = ( os.path.join(BASE_DIR,'static/'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

MEDIA_URL = '/media/'

# collectstatic command will gather static files here
STATIC_ROOT = os.path.join(BASE_DIR, "static_collect")

# Override CSS class for the ERROR tag level to match Bootstrap class name
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.ERROR: 'danger'}

NYT_API_KEY = '675c2c18ffb102513d15141c24b8e19e:8:50612933'

# See https://github.com/shacker/django-todo/wiki/Requirements-and-Installation
TODO_STAFF_ONLY = False
TODO_DEFAULT_ASSIGNEE = 'shack'
TODO_DEFAULT_LIST_ID = 9
TODO_PUBLIC_SUBMIT_REDIRECT = 'dashboard'


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],

    'PAGINATE_BY': 10,                 # Default to 10
    'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100,             # Maximum limit allowed when using `?page_size=xxx`.
}


try:
    from local_settings import *
except ImportError:
    pass
