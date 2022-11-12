from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def get_api(request):
    users = User.objects.all()
    serailized_users = UserSerializer(users, many=True)
    return Response(serailized_users.data)


@api_view(['POST'])
def post_api(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
