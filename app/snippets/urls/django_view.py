from django.urls import path

from ..views import django_view as Views

urlpatterns = [
    path('snippets', Views.snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', Views.snippet_detail, name='snippet-detail'),
]