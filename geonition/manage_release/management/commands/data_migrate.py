from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.management import call_command
from django.core.serializers.base import DeserializationError
import datetime
import json

class Command(BaseCommand):
    help = "The command will migrate dumped data from previous version to current version of releases. Give as an agument the absolute path with a trailing backslash to the folder where the dumped data exists."
    
    def handle(self, *args, **options):
        data_folder = args[0]
        for app in settings.INSTALLED_APPS:
            
            # load dumped data for apps if .json file found
            try:
                jsonfile = open("%s%s.json" % (data_folder, app), 'r')
                new_jsonfile = open("%s%s_new.json" % (data_folder, app), 'w')

                #modify the jsonfile if required for migrating
                if app == 'dashboard':
                    new_json = []                    
                    new_json = remove_field('tooltip', json.loads(jsonfile.read()))

                    for lang in settings.LANGUAGES:
                        lang_code = lang[0]
                        field_name = "tooltip_%s" % lang_code
                        new_json = remove_field(field_name, new_json)
                        
                    new_json = add_field("modify_date", new_json, default_value = datetime.datetime.now().strftime("%Y-%m-%d"))
                    new_jsonfile.write(json.dumps(new_json))
                
                else:
                    new_jsonfile.write(jsonfile.read())
                    
                new_jsonfile.close()
                jsonfile.close()
                    
                #load the modified json file
                call_command('loaddata', app, "%s%s_new.json" % (data_folder, app))
            
            except IOError:
                pass
            except DeserializationError:
                print "Make sure you installed the current version of the applications using >>> sh install_all.sh command"
   
def remove_field(field_name, json_list):
    print "removing field %s" % field_name
    new_list = []
    
    for json_dict in json_list:
        try:
            del json_dict['fields'][field_name]
        except KeyError:
            pass
        new_list.append(json_dict)
        
    return new_list

def add_field(field_name, json_list, default_value = None):
    print "adding new field %s" % field_name
    new_list = []
    
    for json_dict in json_list:
        json_dict['fields'][field_name] = default_value
        new_list.append(json_dict)
        
    return new_list     