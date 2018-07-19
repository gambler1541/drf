from django.urls import path, include

from . import django_view


app_name = 'snippets'

urlpatterns = [
    path('django_view/', include(django_view))
]