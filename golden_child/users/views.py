# from django.shortcuts import render

# # Create your views here.

# from rest_framework import viewsets
# from .serializers import UserSerializer
# from .models


# from django.views import View
# from django.http import HttpResponse, JsonResponse

# class IndexView(View):
#     def get(self, request):
#         dummy_data = {
#             'name': '죠르디',
#             'type': '공룡',
#             'job': '편의점알바생',
#         }
#             'age': 5
#         return JsonResponse(dummy_data)

#     def post(self, request):
#         return HttpResponse("Post 요청을 잘받았다")

#     def put(self, request):
#         return HttpResponse("Put 요청을 잘받았다")

#     def delete(self, request):
#         return HttpResponse("Delete 요청을 잘받았다")

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
