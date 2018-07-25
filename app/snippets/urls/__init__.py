from django.urls import path, include

from . import django_view, api_view, mixins, generic_cbv


app_name = 'snippets'

urlpatterns = [
    path('django_view/', include(django_view)),
    path('api_view/', include(api_view)),
    path('mixins/', include(mixins)),
    path('generic_cbv/', include(generic_cbv)),
]