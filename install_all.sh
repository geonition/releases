# Installs modeltranslation from svn repository to prevent XMLField error in test
pip install svn+http://django-modeltranslation.googlecode.com/svn/trunk/@156
pip install https://github.com/geonition/django_geonition_utils/tarball/4.2.0
pip install https://github.com/geonition/django_auth/tarball/4.0.1
pip install https://github.com/geonition/django_geojson_rest/tarball/5.3.1
pip install https://github.com/geonition/django_opensocial_people/tarball/4.0.1
pip install https://github.com/geonition/django_geonition_client/tarball/4.0.0
pip install https://github.com/geonition/base_page/tarball/master #meta arguments fixed, pylint and feedback template fix for big displays
pip install https://github.com/geonition/dashboard/tarball/master #help text and verbose names in admin, 
pip install https://github.com/geonition/planproposal/tarball/4.2.4
pip install https://github.com/geonition/auth_page/tarball/4.0.4
pip install https://github.com/geonition/geoforms/tarball/master #removed old element adding forms, max amount of features per button feature added, input text space problem fixed with strip(), added textarea support, slug lengths modified and timestamps added supports japanese characters better
pip install https://github.com/geonition/geodjango-map-layers/tarball/4.1.2
pip install https://github.com/geonition/django_images/tarball/4.1.0
pip install django-rosetta
# If needed install new version of lxml
# CFLAGS=-fPIC STATICBUILD=true LIBXML2_VERSION=2.8.0 pip install lxml
