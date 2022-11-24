from django.urls import include, path
from rest_framework import routers
from texts.views import QuestionViewSet, AnswerViewSet, GetOneQuestionView

router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)

app_name = 'texts'

urlpatterns = [
    path('list/', include(router.urls)),
    path('single-question/', GetOneQuestionView.as_view(), name='GetQuestion')
]
