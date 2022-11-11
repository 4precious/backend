# from django.contrib.auth.models import User, Group
# from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

from django.core import serializers
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_parent', 'is_child', 'linked_user']
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    is_parent = serializers.BooleanField()
    is_child = serializers.BooleanField()
    linked_user = serializers.EmailField(allow_blank=True)
