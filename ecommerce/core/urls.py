from django.contrib import admin
from django.urls import path

from ariadne.contrib.django.views import GraphQLView

from core.graphql.config import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(schema=schema))
]
