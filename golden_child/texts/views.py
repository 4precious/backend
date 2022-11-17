# Create your views here.
from rest_framework import viewsets
from texts.serializers import QuestionSerializer, AnswerSerializer
from texts.models import parent_question, child_answer

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = parent_question.objects.all()
    serializer_class = QuestionSerializer
    def perform_create(self, serializer):
        user_info = self.request.user
        if user_info.is_parent == False:
            raise ValueError('Question should be made by parent user')
        else:
            serializer.save(user = self.request.user)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = child_answer.objects.all()
    serializer_class = AnswerSerializer
    def perform_create(self, serializer):
        user_info = self.request.user
        if user_info.is_child == False:
            raise ValueError('Question should be made by child user')
        else:
            serializer.save(user = self.request.user)