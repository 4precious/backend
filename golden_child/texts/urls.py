from django.urls import include, path
from rest_framework import routers
from texts.views import QuestionViewSet, AnswerViewSet

router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)
router.register(r'Answer', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]