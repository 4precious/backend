# serializers.py in the users Django app
from rest_framework import serializers
from .models import User
from django.db import transaction
from rest_auth.registration.serializers import RegisterSerializer

from users.models import USERTYPE

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'user_type', 'linked_user', 'created_at')


class CustomRegisterSerializer(RegisterSerializer):
    user_type = serializers.ChoiceField(choices=USERTYPE)
    linked_user = serializers.EmailField(max_length=254, allow_blank=True)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.user_type = self.data.get('user_type')
        user.linked_user = self.data.get('linked_user')

        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'user_type', 'linked_user', 'created_at')
        