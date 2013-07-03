from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dashboard/', include('dashboard.urls')), # remove after 1.2.2013
    url(r'^', include('dashboard.urls')),
    url(r'^api/client/', include('geonition_client.urls')),
    url(r'^api/geojson/', include('geojson_rest.urls')),
    url(r'^api/auth/', include('gntauth.urls')),
    url(r'^base_page/', include('base_page.urls')),
    url(r'^planning/', include('plan_proposals.urls')),
    url(r'^images/', include('gntimages.urls')),
    url(r'^auth_page/', include('auth_page.urls')),
    url(r'^geoforms/', include('geoforms.urls')),
    url(r'^maps/', include('maps.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^user_media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )