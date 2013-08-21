import os

# Django settings for geonition project.

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'geonition_utils.middleware.PreventCacheMiddleware', #should be only for REST data api
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'geonition_utils.middleware.IEEdgeMiddleware', #should be only for ui html/css apps
)

ROOT_URLCONF = 'geonition.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'geonition.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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

#REQUIRED AND MODIFIED
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#CHANGE TEST RUNNER TO OUR OWN TO DISABLE MODELTRANSLATION TESTS
TEST_RUNNER = 'statics.tests.GeonitionTestSuiteRunner'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.gis',

    #geonition apps
    'base_page',
    'dashboard',
    'maps',
    'auth_page',
    'plan_proposals',
    'geonition_client',
    'gntauth',
    'gntimages',
    'geojson_rest',
    'geonition_utils',
    'geoforms',
    
    # release apps
    'manage_release',
    'statics',
    
    # third party apps
    'modeltranslation',
#    'rosetta',
)

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
"django.core.context_processors.request",
"base_page.context_processors.organization"
)

TEMPLATE_DIRS = (os.path.dirname(os.path.realpath(__file__)) + '/../statics/templates')

JAVASCRIPT_CLIENT_TEMPLATES = [
    'geonition_auth.jquery.js',
    'data_processing.jquery.js',
    'opensocial_people.jquery.js',
    'geonition_geojson.jquery.js',
    'questionnaire.api.js'
]

#Google api
GOOGLE_API_KEY = ''

#MODEL TRANSLATION
#MODELTRANSLATION_TRANSLATION_REGISTRY = "geonition.translation"

from django.core.urlresolvers import reverse_lazy
LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

WSGI_APPLICATION = "geonition.wsgi.application"

#MODELTRANSLATION_TRANSLATION_FILES = ('geonition.translation',)
