import os 
import django

from django.core.wsgi import get_wsgi_application
from ariadne.wsgi import GraphQL, GraphQLMiddleware

from core.graphql.config import schema

from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

settings = os.getenv('DJANGO_SETTINGS_MODULE')

if settings == "core.settings.prod":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.prod')

    django_application = get_wsgi_application()
    graphql_application = GraphQL(schema)
    application = GraphQLMiddleware(django_application, graphql_application)
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.dev')
    application = get_wsgi_application()
