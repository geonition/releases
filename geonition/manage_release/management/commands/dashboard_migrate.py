from optparse import make_option
from django.core.management import call_command
from django.core.management.base import NoArgsCommand, CommandError
from django.core.management.color import no_style
from django.db import models, DEFAULT_DB_ALIAS
from django.db import connections, transaction
from django.conf import settings
from geoforms.models import Questionnaire
from dashboard.models import Project
from django.contrib.gis import geos

class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        make_option('--database', action='store', dest='database',
            default=DEFAULT_DB_ALIAS, help='Nominates a database to update. '
                'Defaults to the "default" database.'),
    )
    def handle_noargs(self, **options):
        
        projects = Project.on_site.all()
        questionnaires = Questionnaire.on_site.all()
        
        self.stdout.write('Found:\n')
        self.stdout.write('{1} project(s)\n'.format(len(projects)))
        self.stdout.write('{1} questionnaire(s)\n'.format(len(questionnaires)))

        if len(projects) == 0 or len(questionnaires) == 0:
            self.stderr.write('No projects or questionnaires found, exiting')
            return
        updated_questionnaires = 0 
        for project in projects:
            # This is the slug of the questionnaire
            d_url = project.project_url.split('/geoforms')[1].strip('/')
            quest = questionnaires.get(slug=d_url)
            #import ipdb; ipdb.set_trace()
            if not quest:
                continue
            #move previous questionnaire area to detailed areas
            if quest.detailed_areas is None:
                quest.detailed_areas = geos.MultiPolygon(quest.area)
                quest.detailed_areas.set_srid(quest.area.srid)
            
            #move dashboard area to questionnaire area
            quest.area = project.location
            
            #add description to the questionnaire
            quest.description = project.description
            for lang in settings.LANGUAGES:
                setattr(quest,
                        'description_' + lang[0],
                        getattr(project, 'description_' + lang[0]))

            quest.save()
            updated_questionnaires =+ 1
            
        self.stdout.write('Updated {1} questionnaire(s)'.format(updated_questionnaires))
            