from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         email=validated_data['email'],
    #         password=validated_data['password'],
    #         linked_user=validated_data['linked_user'],
    #         is_parent=validated_data['is_parent'],
    #         is_child=validated_data['is_child']
    #     )
    #     return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'linked_user',
                  'is_parent', 'is_child', 'created_at')

    linked_user = serializers.EmailField(allow_blank=True)
