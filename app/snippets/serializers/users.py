from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

__all__ = (

    'UserListSerializer',
    'UserDetailSerializer',
)

class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
        )


class UserListSerializer(UserBaseSerializer):
    pass


class UserDetailSerializer(UserBaseSerializer):
    class Meta:
        fields = UserBaseSerializer.Meta.fields + ('snippets',)
