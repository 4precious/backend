from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.UserViewSet)

app_name = 'users'

urlpatterns = [
    path('', include(router.urls))
]
