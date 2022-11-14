# Create your views here.
from rest_framework import viewsets
from texts.serializers import QuestionSerializer, AnswerSerializer
from texts.models import Question, Answer

# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        user_info = self.request.user
        if user_info.get_usertype == 'CHILD' or user_info.get_usertype == 'Child':
            raise ValueError('Question should be made by parent user')
        else:
            serializer.save(user=self.request.user)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        user_info = self.request.user
        if user_info.get_usertype == 'PARENT' or user_info.get_usertype == 'Parent':
            raise ValueError('Answer should be made by child user')
        else:
            serializer.save(user=self.request.user)
