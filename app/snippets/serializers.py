from rest_framework import serializers

from .models import Snippet

__all__ = (
    'SnippetSerializer',
)

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'pk',
            'title',
            'code',
            'linenos',
            'language',
            'style',
        )