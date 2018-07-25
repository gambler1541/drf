from rest_framework import serializers

from snippets.models import Snippet
from .users import UserListSerializer

__all__ = (
    'SnippetBaseSerializer',
    'SnippetDetailSerializer',
    'SnippetListSerializer',

)

class SnippetBaseSerializer(serializers.ModelSerializer):
    owner = UserListSerializer()

    class Meta:
        model = Snippet
        fields = (
            'pk',
            'title',
            'linenos',
            'language',
            'style',
            'owner',
        )
        read_only_fields = (
            'owner',
        )



class SnippetListSerializer(SnippetBaseSerializer):
    pass

class SnippetDetailSerializer(SnippetBaseSerializer):
    class Meta(SnippetBaseSerializer.Meta):
        fields = SnippetBaseSerializer.Meta.fields + ('code',)