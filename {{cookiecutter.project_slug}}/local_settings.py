# pylint: disable=unused-wildcard-import,wildcard-import
import sys

from example.settings import *  # noqa

DEBUG = True

if sys.argv[1] in ['runserver', 'runserver_plus']:
    INSTALLED_APPS += ['debug_toolbar', ]  # noqa
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]  # noqa
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda n: True,
    }
