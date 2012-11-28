# Installs modeltranslation from svn repository to prevent XMLField error in test
pip install svn+http://django-modeltranslation.googlecode.com/svn/trunk/@139
pip install https://github.com/geonition/django_geonition_utils/tarball/4.3.0
pip install https://github.com/geonition/django_auth/tarball/4.1.0
pip install https://github.com/geonition/django_geojson_rest/tarball/master # Translations updated. fixed admin tests
pip install https://github.com/geonition/django_opensocial_people/tarball/4.0.1
pip install https://github.com/geonition/django_geonition_client/tarball/4.0.0
pip install https://github.com/geonition/base_page/tarball/master # Images from libs. Translations updated
pip install https://github.com/geonition/dashboard/tarball/master # Translations updated
pip install https://github.com/geonition/planproposal/tarball/master # Translations updated
pip install https://github.com/geonition/auth_page/tarball/4.0.4
pip install https://github.com/geonition/geoforms/tarball/master # Translations updated
pip install https://github.com/geonition/geodjango-map-layers/tarball/master # Source model for ArcGIS server urls, parses map-services and layers.
# Layer preview. Forms for map creation. get map list as json. Different OpenStreetMap versions. ARCGISRest layers (as overlay) from source url.
pip install https://github.com/geonition/django_images/tarball/4.1.0
pip install django-rosetta
# If needed install new version of lxml
# CFLAGS=-fPIC STATICBUILD=true LIBXML2_VERSION=2.8.0 pip install lxml
