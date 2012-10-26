# Installs modeltranslation from svn repository to prevent XMLField error in test
pip install svn+http://django-modeltranslation.googlecode.com/svn/trunk/@139
pip install https://github.com/geonition/django_geonition_utils/tarball/4.3.0
pip install https://github.com/geonition/django_auth/tarball/4.1.0
pip install https://github.com/geonition/django_geojson_rest/tarball/5.5.0 # all view models uses sama m2m table. m2m field views added to views 
pip install https://github.com/geonition/django_opensocial_people/tarball/4.0.1
pip install https://github.com/geonition/django_geonition_client/tarball/4.0.0
pip install https://github.com/geonition/base_page/tarball/4.6.0 # updated JQuery, JQuery ui and mozernizer. Styles are in index.html. setup changes for OpenLayers.
pip install https://github.com/geonition/dashboard/tarball/5.2.0 
pip install https://github.com/geonition/planproposal/tarball/4.3.0 
pip install https://github.com/geonition/auth_page/tarball/4.0.4
pip install https://github.com/geonition/geoforms/tarball/5.5.0 # JQuery moved to base_page. self.id instead of time in slugs. fallback for html5 slider. paragraphs accept html5 tags. OSM admin works with https
pip install https://github.com/geonition/geodjango-map-layers/tarball/4.1.2
pip install https://github.com/geonition/django_images/tarball/4.1.0
pip install django-rosetta
# If needed install new version of lxml
# CFLAGS=-fPIC STATICBUILD=true LIBXML2_VERSION=2.8.0 pip install lxml
