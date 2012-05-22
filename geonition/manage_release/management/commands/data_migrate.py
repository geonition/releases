from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.management import call_command
import json
import shutil

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        data_folder = args[0]
        for app in settings.INSTALLED_APPS:
            
            # load dumped data for apps if .json file found
            try:
                shutil.copyfile( "%s%s.json" % (data_folder, app), "%s%s.json~" % (data_folder, app) )
                jsonfile = open("%s%s.json~" % (data_folder, app), 'r')
                new_jsonfile = open("%s%s.json" % (data_folder, app), 'w')

                #modify the jsonfile if required for migrating
                if app == 'geoforms':
                    json_obj = json.loads(jsonfile.read())
                    new_json = []
                    for obj in json_obj:
                        try:
                            del obj['fields']['lang']
                        except KeyError:
                            pass
                        new_json.append(obj)
                    new_jsonfile.write(json.dumps(new_json))
                    new_jsonfile.close()
                    jsonfile.close()
                    
                #load the modified json file
                try:
                    call_command('loaddata', app, "%s%s.json" % (data_folder, app))
                except:
                    pass
            
            except Exception:
                pass
        