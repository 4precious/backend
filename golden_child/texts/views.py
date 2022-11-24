# Create your views here.
from rest_framework import viewsets
from texts.serializers import QuestionSerializer, AnswerSerializer
from texts.models import Question, Answer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        user_type = self.request.user.user_type
        if user_type == 'CHILD' or user_type == 'Child':
            raise ValueError('Question should be made by parent user')

        serializer.save(user=self.request.user)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        user_type = self.request.user.user_type
        if user_type == 'PARENT' or user_type == 'Parent':
            raise ValueError('Answer should be made by child user')

        serializer.save(user=self.request.user)


class GetOneQuestionView(APIView):
    def post(self, request, **kwargs):
        email = kwargs.get('email')
        serializer = QuestionSerializer(Question.objects.get(user_email=email))

        # queryset = Question.objects.filter(user_email=request.email).values()
        return Response(serializer.data)
