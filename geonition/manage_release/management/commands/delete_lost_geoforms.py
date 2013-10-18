from django.core.management.base import NoArgsCommand, CommandError
from questionnaire_admin.utils import copyQuestionnaireForms
from questionnaire_admin.models import GeoformLock,GeoformElementLock
from geoforms.models import Geoform,GeoformElement,Questionnaire,QuestionnaireForm,FormElement
from bs4 import BeautifulSoup

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        print 'deleting geoforms and geoformelements that are locked (i.e. copied) but whose questionnaire exists no more'
        locked_geoforms = Geoform.objects.filter(page_type="form").exclude(geoformlock=None)
        locked_elements = GeoformElement.objects.all().exclude(geoformelementlock=None)
        for g in locked_geoforms:
            if QuestionnaireForm.objects.filter(geoform=g).exists():
                print 'geoform %s in questionnaire' % g.name
            else:
                g.delete()
        for ge in locked_elements:
            if FormElement.objects.filter(element=ge).exists():
                print 'element %s in a geoform' % ge.name
            else:
                ge.delete()
        locked_popups = Geoform.objects.filter(page_type="popup").exclude(geoformlock=None)
        for p in locked_popups:
            popup_is_lost = True
            for ge in GeoformElement.objects.filter(element_type="drawbutton"):
                popup_slug = BeautifulSoup(ge.html).button['data-popup']
                if popup_slug == p.slug:
                    popup_is_lost = False
                    break
            if popup_is_lost:
                p.delete()
            else:
                print 'popup %s is connected to a geoform element' % p.name
        # re-run after lost popups have been deleted
        locked_elements = GeoformElement.objects.all().exclude(geoformelementlock=None)
        for ge in locked_elements:
            if FormElement.objects.filter(element=ge).exists():
                print 'element %s in a geoform' % ge.name
            else:
                ge.delete()
