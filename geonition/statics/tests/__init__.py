from django.conf import global_settings, settings
from django.test.simple import DjangoTestSuiteRunner
from django.test.simple import build_suite, build_test
from django.utils import unittest
from django.db.models.loading import get_models
from django.core.management import call_command

from optparse import make_option

class GeonitionTestSuiteRunner(DjangoTestSuiteRunner):
    """
    This testrunner makes some settings changes to make Django tests pass
    """
        # option_list = (
        # make_option('--modeltranslation', action='store_true', default=False,
            # help='Test modeltranslation application, default is False'),
    # )
    # def __init__(self, verbosity=1, interactive=True, failfast=True, modeltranslation=False, **kwargs):
        # super(GeonitionTestSuiteRunner, self).__init__(
            # verbosity=verbosity, interactive=interactive, failfast=failfast, **kwargs)
        # self.modeltranslation = modeltranslation
#         
    def setup_test_environment(self, **kwargs):
        
        super(GeonitionTestSuiteRunner, self).setup_test_environment(**kwargs)
        
        self.old_login_redict_url = getattr(settings, 'LOGIN_REDIRECT_URL', None)
        self.old_login_url = getattr(settings, 'LOGIN_URL', None)
        self.old_logout_url = getattr(settings, 'LOGOUT_URL', None)
        
#        settings.LOGIN_REDIRECT_URL = getattr(global_settings, 'LOGIN_REDIRECT_URL')
#        settings.LOGIN_URL = getattr(global_settings, 'LOGIN_URL')
#        settings.LOGOUT_URL = getattr(global_settings, 'LOGOUT_URL')
        
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
    def teardown_test_environment(self, **kwargs):
        super(GeonitionTestSuiteRunner, self).teardown_test_environment(**kwargs)

        settings.LOGIN_REDIRECT_URL = self.old_login_redict_url
        settings.LOGIN_URL = self.old_login_url
        settings.LOGOUT_URL = self.old_logout_url
        # settings.INSTALLED_APPS = self.old_installed_apps
        
        
    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        # from django.db.models import get_app
        
        # suite = unittest.TestSuite()
        
        if 'auth' in test_labels or 'django.contrib.auth' in settings.INSTALLED_APPS:
            settings.LOGIN_REDIRECT_URL = getattr(global_settings, 'LOGIN_REDIRECT_URL')
            settings.LOGIN_URL = getattr(global_settings, 'LOGIN_URL')
            settings.LOGOUT_URL = getattr(global_settings, 'LOGOUT_URL')
            
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
            
        
    def setup_databases(self, **kwargs):
        old_names, mirrors = super(GeonitionTestSuiteRunner, self).setup_databases(**kwargs)

        #Call syncdb second time to create custom views with geometrycolumn
        #First run still gives sql errors about geometrycolumns
        # Get correct connection object
        con = old_names[0][0] 
        call_command('syncdb',
            verbosity=max(self.verbosity - 1, 0),
            interactive=False,
            database=con.alias,
            load_initial_data=False)
                        
        return old_names, mirrors

# create django_jenkins testrunner, there might be a better way to check if django_jenkis is in installed apps
if 'django_jenkins' in settings.INSTALLED_APPS:
    from django_jenkins.runner import CITestSuiteRunner
    class GeonitionJenkinsTestSuiteRunner(CITestSuiteRunner):
        """
        This testrunner makes some settings changes to make Django tests pass
        """
            # option_list = (
            # make_option('--modeltranslation', action='store_true', default=False,
                # help='Test modeltranslation application, default is False'),
        # )
        # def __init__(self, verbosity=1, interactive=True, failfast=True, modeltranslation=False, **kwargs):
            # super(GeonitionTestSuiteRunner, self).__init__(
                # verbosity=verbosity, interactive=interactive, failfast=failfast, **kwargs)
            # self.modeltranslation = modeltranslation
    #         
        def setup_test_environment(self, **kwargs):
            
            super(GeonitionJenkinsTestSuiteRunner, self).setup_test_environment(**kwargs)
            
            self.old_login_redict_url = getattr(settings, 'LOGIN_REDIRECT_URL', None)
            self.old_login_url = getattr(settings, 'LOGIN_URL', None)
            self.old_logout_url = getattr(settings, 'LOGOUT_URL', None)
            
    #        settings.LOGIN_REDIRECT_URL = getattr(global_settings, 'LOGIN_REDIRECT_URL')
    #        settings.LOGIN_URL = getattr(global_settings, 'LOGIN_URL')
    #        settings.LOGOUT_URL = getattr(global_settings, 'LOGOUT_URL')
            
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
        def teardown_test_environment(self, **kwargs):
            super(GeonitionJenkinsTestSuiteRunner, self).teardown_test_environment(**kwargs)
    
            settings.LOGIN_REDIRECT_URL = self.old_login_redict_url
            settings.LOGIN_URL = self.old_login_url
            settings.LOGOUT_URL = self.old_logout_url
            # settings.INSTALLED_APPS = self.old_installed_apps
            
            
        def build_suite(self, test_labels, extra_tests=None, **kwargs):
            # from django.db.models import get_app
            
            # suite = unittest.TestSuite()
            
            if 'auth' in test_labels or 'django.contrib.auth' in settings.INSTALLED_APPS:
                settings.LOGIN_REDIRECT_URL = getattr(global_settings, 'LOGIN_REDIRECT_URL')
                settings.LOGIN_URL = getattr(global_settings, 'LOGIN_URL')
                settings.LOGOUT_URL = getattr(global_settings, 'LOGOUT_URL')
                
            if test_labels:
                return super(GeonitionJenkinsTestSuiteRunner, self).build_suite(
                         test_labels, extra_tests=extra_tests, **kwargs)
    
            new_test_labels = []
            for app in settings.INSTALLED_APPS:
                parts = app.split('.')
                app_name = parts[-1]
                if not app_name == 'modeltranslation':
                    new_test_labels.append(app_name)
    
            return super(GeonitionJenkinsTestSuiteRunner, self).build_suite(
                     tuple(new_test_labels), extra_tests=extra_tests, **kwargs)
                
            
        def setup_databases(self, **kwargs):
            old_names, mirrors = super(GeonitionJenkinsTestSuiteRunner, self).setup_databases(**kwargs)
    
            #Call syncdb second time to create custom views with geometrycolumn
            #First run still gives sql errors about geometrycolumns
            # Get correct connection object
            con = old_names[0][0] 
            call_command('syncdb',
                verbosity=max(self.verbosity - 1, 0),
                interactive=False,
                database=con.alias,
                load_initial_data=False)
                            
            return old_names, mirrors
        
