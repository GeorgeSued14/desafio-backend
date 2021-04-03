"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os 

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv()

settings = os.getenv('DJANGO_SETTINGS_MODULE')

if settings == "core.settings.prod":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.prod')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.dev')

application = get_wsgi_application()
