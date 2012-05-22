from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.management import call_command
import json

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        data_folder = args[0]
        for app in settings.INSTALLED_APPS:
            
            # load dumped data for apps if .json file found
            try:
                jsonfile = open("%s%s.json" % (data_folder, app), 'rw')
                #modify the jsonfile if required for migrating
                if app == 'geoforms':
                    json_obj = json.loads(jsonfile.read())
                    for obj in json_obj:
                        try:
                            del obj['fields']['lang']
                        except KeyError:
                            pass
                    json_file.write(json.dumps(json_obj))
                
                #load the modified json file
                call_command('loaddata', app, "%s%s.json" % (data_folder, app))
            
            except:
                pass
        