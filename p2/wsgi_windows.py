import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# add python site packages, you can use virtualenvs also
site.addsitedir("C:/Users/fujitsu/PycharmProjects/p2/venv/Lib/site-packages")

# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Users/fujitsu/pycharmprojects/p2')
sys.path.append('C:/Users/fujitsu/pycharmprojects/p2/p2')

os.environ['DJANGO_SETTINGS_MODULE'] = 'p2.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "p2.settings")

application = get_wsgi_application()
