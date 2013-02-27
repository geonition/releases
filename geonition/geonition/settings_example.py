from settings.base import *

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a(oav_%x)udnsh5w$=4@+pyxp93ys%c9wa8ck(=22_1d*w2gws'

ADMINS = (
    ('firstname lastname', 'firstname.lastname@somewhere.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',               # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = ''

# Default is 4326(WGS84). This is here for backwards compatibility
# For new installations keep this unchanged, unless you know what you are doing.  
SPATIAL_REFERENCE_SYSTEM_ID = 4326

LANGUAGES = (('en', 'English'),)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

# If using language not in Django base translation set this to directory
# where translations are located
# LOCALE_PATHS = ()
 
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

SITE_ID = 1

DEBUG = True

TEMPLATE_DEBUG = DEBUG

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

POSTGIS_VERSION = (1, 5, 3)

POSTGIS_TEMPLATE = 'postgis_template'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

#Google api
GOOGLE_API_KEY = ''

ORGANIZATION_ADMIN_DEFAULT_MAP_SETTINGS = {'default_lon': 0,
                                           'default_lat': 0,
                                           'default_zoom': 4}
