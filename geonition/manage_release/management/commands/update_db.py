from optparse import make_option
from django.core.management import call_command
from django.core.management.base import NoArgsCommand, CommandError
from django.core.management.color import no_style
from django.db import models, DEFAULT_DB_ALIAS
from django.db import connections, transaction
#from geojson_rest.sql import *
from manage_release.schema_update import schema_changes

class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        make_option('--database', action='store', dest='database',
            default=DEFAULT_DB_ALIAS, help='Nominates a database to synchronize. '
                'Defaults to the "default" database.'),
    )
    def handle_noargs(self, **options):
        
        
        db = options.get('database')
        connection= connections[db]
        cursor = connection.cursor()
        introspection = connection.introspection
        
        # get the latest revision
        cur_rev = schema_changes.pop()
#        if cur_rev == 'master':
#            print
        apps = cur_rev[1]
        
        for app in apps:
            cur_app = app[0]
            print ('SQL to execute for application %s:' % cur_app)
            for sql in app[1]:
                print sql
            for sql in app[1]:
                try:
                    cursor.execute(sql)
                except Exception as e:
#                    import ipdb; ipdb.set_trace()
#                    self.stdout.write(sql)
                    self.stderr.write(e.message)
                    self.stderr.write("Database for application %s is allready updated.\n" % cur_app)
                    transaction.rollback_unless_managed(using=db)
                    break
            transaction.commit_unless_managed(using=db)            
            print('--------------------------------------------------------------------------------------')
                
            
        
        
        # Create customs views for geojson_rest
#         if 'geojson_rest' in settings.INSTALLED_APPS:
#             app = models.get_app('geojson_rest')
#             app_models = models.get_models(app, include_auto_created=True)
#             tables = connection.introspection.table_names()
#             converter = connection.introspection.table_name_converter
#             import ipdb; ipdb.set_trace()
#             
#             custom_sql = sql_custom(models.get_app('geojson_rest'), no_style, connection)
#             
#             #self.stdout.write(custom_sql)
#             if custom_sql:
#                 cursor = connection.cursor()
#                 try:
#                     for sql in custom_sql:
#                         cursor.execute(sql)
#                 except Exception as e:
#                     self.stdout.write(sql)
#                     self.stderr.write("Failed to install custom SQL for geojson_rest: %s\n" % e)
#                     transaction.rollback_unless_managed(using=db)
#                 else:
#                     transaction.commit_unless_managed(using=db)            
# 
#         # Load initial_data fixtures (unless that has been disabled)
#         if orig_load_initial_data:
#             call_command('loaddata', 'initial_data', verbosity=verbosity,
#                          database=db, skip_validation=True)            