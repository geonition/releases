from django.core.management import setup_environ
import settings

setup_environ(settings)

jsonfile = open("data/geojson_rest.json")

import json

json_list = json.loads(jsonfile.read())

jsonfile.close()

def remove_field(field_name, json_list):
    print "removing field %s" % field_name
    new_list = []
    
    for json_dict in json_list:
        del json_dict['fields'][field_name]
        new_list.append(json_dict)
        
    return new_list

def add_field(field_name, default_value = None):
    print "adding new field %s" % field_name
    new_list = []
    
    for json_dict in json_list:
        json_dict['fields'][field_name] = default_value
        new_list.append(json_dict)
        
    return new_list

