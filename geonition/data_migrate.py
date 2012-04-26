from django.core.management import setup_environ
from geonition import settings

setup_environ(settings)

jsonfile = open("../data/geojson_rest.json")
print jsonfile

import json

json_list = json.loads(jsonfile.read())

jsonfile.close()

data_dict = {}

for obj in json_list:
    if obj['model'] == 'geojson_rest.feature':
        data_dict[obj['pk']] = {}
        data_dict[obj['pk']]['feature'] = obj['fields']


for obj in json_list:
    if obj['model'] == 'geojson_rest.property':
        data_dict[obj['pk']]['property'] = obj['fields']


from geojson_rest.models import Feature
from geojson_rest.models import Property
from django.db import models
from django.conf import settings
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.gdal import OGRGeometry
from django.contrib.auth.models import User
from geonition_utils.models import JSON
from geonition_utils.models import TimeD

for key, value in data_dict.items():
    print key
    print value

    #create feature
    feature = value['feature']
    geometry = OGRGeometry(feature['geometry']).geos
    private = feature.get('private', True)
    user = User.objects.get(id = feature['user'])
    group = 'PP-perhela-perhelan-kortteli' #they are all put into the same group Jarvenpaa
    time = TimeD(create_time = feature['create_time'],
                 expire_time = feature['expire_time'])
    time.save()
    new_feature = Feature(geometry = geometry,
                          user = user,
                          group = group,
                          private = private,
                          time = time)
    new_feature.save()

    #create property
    timed = TimeD()
    timed.save()
    time = timed
    prop = Property()
    #self.properties.add(prop)

