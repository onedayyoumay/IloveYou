import os
import sys

sys.path.append('/var/www/Slow/mysite')

os.environ['PYTHON_EGG_CACHE'] = '/var/www/Slow/.python-egg'

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
