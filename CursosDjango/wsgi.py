import os
import sys

path = os.path.expanduser('~/Charliedev-11095/CursoDjango')
if path not in sys.path:
    sys.path.insert(0,path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CursosDjango.settings')
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = get_wsgi_application()