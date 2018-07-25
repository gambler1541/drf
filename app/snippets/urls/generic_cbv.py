from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from ..views import generic_cbv as Views

urlpatterns = [
    path('snippets/', Views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', Views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', Views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', Views.UserDetail.as_view(), name='user-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
