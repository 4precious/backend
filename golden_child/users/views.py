from rest_framework import viewsets
from .models import User
#from .serializers import CustomRegisterSerializer
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    #serializer_class = CustomRegisterSerializer
    serializer_class = UserSerializer
