from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

app_name = 'users'

urlpatterns = [
    path('user-list/', include(router.urls)),
    path('current-user/', views.CurrentUserView.as_view(), name='CurrentUser')
]
