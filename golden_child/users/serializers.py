from rest_framework import serializers
from .models import User
from rest_auth.registration.serializers import RegisterSerializer



# class UserSerializer(serializers.ModelSerializer):
#     # def create(self, validated_data):
#     #     user = User.objects.create_user(
#     #         email=validated_data['email'],
#     #         password=validated_data['password'],
#     #         linked_user=validated_data['linked_user'],
#     #         is_parent=validated_data['is_parent'],
#     #         is_child=validated_data['is_child']
#     #     )
#     #     return user

#     class Meta:
#         model = User
#         fields = ('id', 'email', 'password', 'linked_user',
#                   'is_parent', 'is_child', 'created_at')

#     linked_user = serializers.EmailField(allow_blank=True)

class CustomRegisterSerializer(RegisterSerializer):
    is_child = serializers.BooleanField(default=False)
    is_parent = serializers.BooleanField(default=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['is_child'] = self.validated_data.get('is_child', '')
        data['is_parent'] = self.validated_data.get('is_parent', '')

        return data