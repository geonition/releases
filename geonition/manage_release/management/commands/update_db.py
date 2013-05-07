from optparse import make_option
from django.core.management import call_command
from django.core.management.base import NoArgsCommand, CommandError
from django.core.management.color import no_style
from django.db import models, DEFAULT_DB_ALIAS
from django.db import connections, transaction
from django.conf import settings
#from geojson_rest.sql import *
from manage_release.schema_update import schema_changes

class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        make_option('--database', action='store', dest='database',
            default=DEFAULT_DB_ALIAS, help='Nominates a database to update. '
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
            if cur_app in settings.INSTALLED_APPS:
                print ('SQL to execute for application %s:' % cur_app)
    #            for sql in app[1]:
    #                print sql
                for sql in app[1]:
                    try:
                        cursor.execute(sql)
                    except Exception as e:
    #                    import ipdb; ipdb.set_trace()
    #                    self.stdout.write(sql)
                        self.stderr.write(e.message)
                        self.stderr.write("SQL: {} for application {} is allready applied.\n".format(sql, cur_app))
                        transaction.rollback_unless_managed(using=db)
                transaction.commit_unless_managed(using=db)            
                print('--------------------------------------------------------------------------------------')
                
