from modeltranslation.translator import translator, TranslationOptions
from base_page.models import OrganizationSetting
from dashboard.models import Project as DashboardProject
from geoforms.models import Questionnaire
from geoforms.models import Geoform
from geoforms.models import GeoformElement
from geoforms.models import QuestionnaireForm
from geoforms.models import TextElementModel
from geoforms.models import FormElement

#base_page
class OrganizationSettingTranslationOptions(TranslationOptions):
    fields = ('organization_name',
              'title',
              'blurb',
              'provider',
              )

translator.register(OrganizationSetting, OrganizationSettingTranslationOptions)

#dashboard
class DashboardProjectTranslationOptions(TranslationOptions):
    fields = ('title',
              'description',
              )

translator.register(DashboardProject, DashboardProjectTranslationOptions)

#geoforms
class QuestionnaireTranslationOptions(TranslationOptions):
    fields = ('name',
              'description',
              )
    
translator.register(Questionnaire, QuestionnaireTranslationOptions)

class GeoformTranslationOptions(TranslationOptions):
    fields = ('name',)
    
translator.register(Geoform, GeoformTranslationOptions)

class GeoformElementTranslationOptions(TranslationOptions):
    fields = ('name',
              'html',)
    
translator.register(GeoformElement, GeoformElementTranslationOptions)
translator.register(TextElementModel, GeoformElementTranslationOptions)

class EmptyTranslationOptions(TranslationOptions):
    fields = ()

translator.register(QuestionnaireForm, EmptyTranslationOptions)
translator.register(FormElement, EmptyTranslationOptions)
