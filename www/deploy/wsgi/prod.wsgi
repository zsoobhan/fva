import os
import sys
import site
from django.core.wsgi import get_wsgi_application

sys.stdout = sys.stderr

# Project root
root = '/var/www/fva/fva/builds/prod/'
sys.path.insert(0, root)

# Packages from virtualenv
activate_this = '/var/www/fva/fva/virtualenvs/prod/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# Set environmental variable for Django and fire WSGI handler 
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ['DJANGO_CONF'] = 'conf.prod'
os.environ["CELERY_LOADER"] = "django"
_application = get_wsgi_application() 

def application(environ, start_response):
    environ['wsgi.url_scheme'] = environ.get('HTTP_X_FORWARDED_PROTO', 'http')
    if environ['wsgi.url_scheme'] == 'https':
        environ['HTTPS'] = 'on'
    return _application(environ, start_response)
