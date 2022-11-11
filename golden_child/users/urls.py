from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    # path('', views.index, name='index'),
    path('get/', views.get_api),
    path('create/', views.post_api),
]
