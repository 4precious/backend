# serializers.py in the users Django app
from rest_framework import serializers
from .models import User
from django.db import transaction
from rest_auth.registration.serializers import RegisterSerializer

from users.models import USERTYPE


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
        fields = ('id', 'email', 'password', 'user_type', 'linked_user',
                  'created_at')


# class CustomRegisterSerializer(RegisterSerializer):
#     is_child = serializers.BooleanField(default=False)
#     is_parent = serializers.BooleanField(default=False)

#     def get_cleaned_data(self):
#         data = super().get_cleaned_data()
#         data['is_child'] = self.validated_data.get('is_child', '')
#         data['is_parent'] = self.validated_data.get('is_parent', '')

#         return data
