from settings.base import *

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a(oav_%x)udnsh5w$=4@+pyxp93ys%c9wa8ck(=22_1d*w2gws'

ADMINS = (
    ('firstname lastname', 'firstname.lastname@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'testdb',                      # Or path to database file if using sqlite3.
        'USER': 'test_user',                      # Not used with sqlite3.
        'PASSWORD': 'test_pw',               # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = '/home/msjohans/geonition_test/media'

#SPATIAL_REFERENCE_SYSTEM_ID = 3067
SPATIAL_REFERENCE_SYSTEM_ID = 3857

LANGUAGES = (('en', 'English'),
             ('fi', 'Suomi'),)

#LANGUAGES = (('de', 'English'),
#             ('en', 'English'),)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'
#LANGUAGE_CODE = 'de'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Helsinki'

SITE_ID = 1

DEBUG = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DEBUG = DEBUG

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/msjohans/geonition_test/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

POSTGIS_VERSION = (1, 5, 3)

POSTGIS_TEMPLATE = 'postgis_template'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

ORGANIZATION_ADMIN_DEFAULT_MAP_SETTINGS = {'default_lon': 0,
                                           'default_lat': 0,
                                           'default_zoom': 4}
# for django-jenkins
INSTALLED_APPS += ('django_jenkins',)
INSTALLED_APPS += ('django_extensions',)
PROJECT_APPS = [appname for appname in INSTALLED_APPS if not (appname.startswith('django') or appname.startswith('modeltranslation'))]
JENKINS_TEST_RUNNER = 'statics.tests.GeonitionJenkinsTestSuiteRunner'
JENKINS_TASKS = (
        'django_jenkins.tasks.with_coverage',
        'django_jenkins.tasks.run_pylint',
        'django_jenkins.tasks.django_tests',   # select one django or
        #'django_jenkins.tasks.dir_tests'      # directory tests discovery
        'django_jenkins.tasks.run_pep8',
#		'django_jenkins.tasks.run_pyflakes',
        'django_jenkins.tasks.run_jshint',
#		'django_jenkins.tasks.run_csslint',    
#		'django_jenkins.tasks.run_sloccount',
        'django_jenkins.tasks.run_graphmodels',   
#		'django_jenkins.tasks.lettuce_tests',
)

