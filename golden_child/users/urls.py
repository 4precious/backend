from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

app_name = 'users'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('get/', views.get_api),
    # path('create/', views.post_api),
    path('', include(router.urls))
]
