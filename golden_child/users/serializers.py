from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'linked_user',
                  'is_parent', 'is_child', 'created_at')

    linked_user = serializers.EmailField(allow_blank=True)
