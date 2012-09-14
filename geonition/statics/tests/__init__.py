from django.conf import settings
from django.test.simple import DjangoTestSuiteRunner
from django.test.simple import build_suite, build_test
from django.utils import unittest

from optparse import make_option

class GeonitionTestSuiteRunner(DjangoTestSuiteRunner):
    # option_list = (
        # make_option('--modeltranslation', action='store_true', default=False,
            # help='Test modeltranslation application, default is False'),
    # )
    # def __init__(self, verbosity=1, interactive=True, failfast=True, modeltranslation=False, **kwargs):
        # super(GeonitionTestSuiteRunner, self).__init__(
            # verbosity=verbosity, interactive=interactive, failfast=failfast, **kwargs)
        # self.modeltranslation = modeltranslation
#         
    # def setup_test_environment(self, **kwargs):
        # super(GeonitionTestSuiteRunner, self).setup_test_environment(**kwargs)
        # self.old_installed_apps = getattr(settings, 'INSTALLED_APPS', None)
#         
        # new_installed_apps= []
# 
        # if self.modeltranslation:
            # new_installed_apps.append('modeltranslation')
#             
        # else:
            # for app in self.old_installed_apps:
                # if not app == 'modeltranslation':
                    # new_installed_apps.append(app)
#                 
        # settings.INSTALLED_APPS = tuple(new_installed_apps)
        # print (settings.INSTALLED_APPS)
        # import ipdb; ipdb.set_trace()
#
    # def teardown_test_environment(self, **kwargs):
        # super(GeonitionTestSuiteRunner, self).teardown_test_environment(**kwargs)
        # #settings.INSTALLED_APPS = self.old_installed_apps
        
    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        # from django.db.models import get_app
        
        # suite = unittest.TestSuite()
        
        
        if test_labels:
            return super(GeonitionTestSuiteRunner, self).build_suite(
                     test_labels, extra_tests=extra_tests, **kwargs)

        new_test_labels = []
        for app in settings.INSTALLED_APPS:
            parts = app.split('.')
            app_name = parts[-1]
            if not app_name == 'modeltranslation':
                new_test_labels.append(app_name)

        return super(GeonitionTestSuiteRunner, self).build_suite(
                 tuple(new_test_labels), extra_tests=extra_tests, **kwargs)
            
        
        