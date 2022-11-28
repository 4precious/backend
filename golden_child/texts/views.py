# Create your views here.
from rest_framework import viewsets
from texts.serializers import QuestionSerializer, AnswerSerializer
from users.models import User
from texts.models import Question, Answer
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import datetime
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from ai.inference import KoBERT, BERTDataset, BERTClassifier

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
        content = self.request.data.get('content')
        KoBERT_model = KoBERT('../../ai/KoBERT_model.pt')
        prediction = KoBERT_model.predict(content)
        print(prediction)
        serializer.save(user=self.request.user)


class GetOneQuestionView(APIView):
    def post(self, request):
        #body_unicode = request.data.decode('utf-8')
        #body = json.loads(body_unicode)
        body = request.data
        email = body['user_email']  # get user_email from body
        created_at = body['date']
        created_at_datetime = datetime.datetime.strptime(
            created_at, '%Y-%m-%d')
        user = User.objects.get(email=email)
        serializer = QuestionSerializer(
            Question.objects.filter(user=user, created_at__year=created_at_datetime.year, created_at__month=created_at_datetime.month, created_at__day=created_at_datetime.day), many=True)

        # queryset = Question.objects.filter(user_email=request.email).values()
        return Response(serializer.data)


class GetOneAnswerView(APIView):
    def get(self, request):
        if not 'question_id' in request.GET:
            raise ValueError('Please enter a question_id')
        # get question from query string
        question_id = request.GET['question_id']
        # print(question_id)
        serializer = AnswerSerializer(
            Answer.objects.filter(question=question_id).latest('created_at'))

        return Response(serializer.data)
