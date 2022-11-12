# Create your views here.
from rest_framework import viewsets
from texts.serializers import QuestionSerializer, AnswerSerializer
from texts.models import parent_question, child_answer

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = parent_question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = child_answer.objects.all()
    serializer_class = AnswerSerializer