import os,sys
import django
root_directory=os.path.abspath(os.path.join(os.path.abspath(__file__),"../../"))
sys.path.append(root_directory)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_template.settings')
django.setup()