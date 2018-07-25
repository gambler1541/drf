from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Snippet

User= get_user_model()

__all__ = (
    'SnippetSerializer',
    'UserSerializer',
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'snippets'
        )


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = (
            'pk',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'owner',
        )
        read_only_fields = (
            'owner',
        )