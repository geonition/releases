# Installs modeltranslation from svn repository to prevent XMLField error in test
pip install svn+http://django-modeltranslation.googlecode.com/svn/trunk/@139
pip install https://github.com/geonition/django_geonition_utils/tarball/master #html5 widgets added
pip install https://github.com/geonition/django_auth/tarball/master #Fixed tests
pip install https://github.com/geonition/django_geojson_rest/tarball/master # pointfeature, polygonfeature, linestringfeature views added (They break the tests)
pip install https://github.com/geonition/django_opensocial_people/tarball/4.0.1
pip install https://github.com/geonition/django_geonition_client/tarball/4.0.0
pip install https://github.com/geonition/base_page/tarball/master #city name changed to organization
pip install https://github.com/geonition/dashboard/tarball/master #city name changed to organization
pip install https://github.com/geonition/planproposal/tarball/master #city name changed to organization
pip install https://github.com/geonition/auth_page/tarball/4.0.4
pip install https://github.com/geonition/geoforms/tarball/master #html5 widgets moved to geonition_utils
pip install https://github.com/geonition/geodjango-map-layers/tarball/4.1.2
pip install https://github.com/geonition/django_images/tarball/4.1.0
pip install django-rosetta
# If needed install new version of lxml
# CFLAGS=-fPIC STATICBUILD=true LIBXML2_VERSION=2.8.0 pip install lxml
