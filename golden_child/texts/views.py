# Create your views here.
from rest_framework import viewsets
from texts.serializers import QuestionSerializer, AnswerSerializer
from users.models import User
from texts.models import Question, Answer
from rest_framework.views import APIView
from rest_framework.response import Response
import json

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
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email = body['user_email']  # get user_email from body
        user = User.objects.get(email=email)
        serializer = QuestionSerializer(
            Question.objects.filter(user=user).latest('created_at'))

        # queryset = Question.objects.filter(user_email=request.email).values()
        return Response(serializer.data)


class GetOneAnswerView(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        question_id = body['question']  # get question from body
        # question = Question.objects.get(id=question_id)
        print(question_id)
        serializer = AnswerSerializer(
            Answer.objects.filter(question=question_id).latest('created_at'))

        # queryset = Question.objects.filter(user_email=request.email).values()
        return Response(serializer.data)
