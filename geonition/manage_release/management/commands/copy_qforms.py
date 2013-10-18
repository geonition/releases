from django.core.management.base import NoArgsCommand, CommandError
from questionnaire_admin.utils import copyQuestionnaireForms

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        print 'copying questionnaire forms'
        copyQuestionnaireForms()
