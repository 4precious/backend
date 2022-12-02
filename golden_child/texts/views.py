# Create your views here.
from rest_framework import viewsets
from texts.serializers import QuestionSerializer, AnswerSerializer, SentimentSerializer
from users.models import User
from texts.models import Question, Answer
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.http import JsonResponse
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
        max_sentiment_key = max(prediction, key=prediction.get)

        self.request.result_happiness = round(prediction['기쁨'], 2)
        self.request.result_anxiety = round(prediction['불안'], 2)
        self.request.result_embarrassment = round(prediction['당황'], 2)
        self.request.result_sadness = round(prediction['슬픔'], 2)
        self.request.result_anger = round(prediction['분노'], 2)
        self.request.result_injury = round(prediction['상처'], 2)
        self.request.result_max_sentiment = max_sentiment_key + ' ' + str(round(prediction[max_sentiment_key], 2))
        
        serializer.save(user=self.request.user, result_happiness=self.request.result_happiness, result_anxiety=self.request.result_anxiety, result_embarrassment=self.request.result_embarrassment, result_sadness=self.request.result_sadness, result_anger=self.request.result_anger, result_injury=self.request.result_injury, result_max_sentiment=self.request.result_max_sentiment)


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
        print(Question.objects.filter(user=user, created_at__year=created_at_datetime.year, created_at__month=created_at_datetime.month, created_at__day=created_at_datetime.day))
        # queryset = Question.objects.filter(user_email=request.email).values()
        return Response(serializer.data)


class GetOneAnswerView(APIView):
    def get(self, request):
        if not 'question_id' in request.GET:
            raise ValueError('Please enter a question_id')
        # get question from query string
        question_id = request.GET['question_id']
        # print(question_id)
        print(Answer.objects.filter(question=question_id).latest('created_at'))
        serializer = AnswerSerializer(
            Answer.objects.filter(question=question_id).latest('created_at'))
        

        return Response(serializer.data)


class GetNUGUReply(APIView):
    def post(self, request):
        # actions
        ACTION_ASKSENTIMENT = 'action.askSentiment'
        # ACTION_HEARAUDIOBOOK = 'action.hearAudioBook'

        body = request.data
        action_name = body['action']['actionName']  # get action name NUGU
        parameters = body['action']['parameters']

        if action_name == ACTION_ASKSENTIMENT:
            print("ACTION_ASKSENTIMENT")
            user = User.objects.get(user_type='CHILD')
            requested_date = parameters['requestedDate']['value']
            if requested_date == '오늘':
                created_at = datetime.datetime.now().strftime('%Y-%m-%d')
                created_at_datetime = datetime.datetime.strptime(created_at, '%Y-%m-%d')
            elif requested_date == '어제':
                created_at_datetime = (datetime.datetime.now() - datetime.timedelta(days=1))
                created_at.strftime('%Y-%m-%d')

            serializer = SentimentSerializer(
                Answer.objects.filter(user=user, created_at__year=created_at_datetime.year, created_at__month=created_at_datetime.month, created_at__day=created_at_datetime.day), many=True
            )

            response = {
                "version": "2.0",
                "resultCode": "OK",
                "output": serializer.data[0],
            }

            return JsonResponse(response)
        # elif action_name == ACTION_HEARAUDIOBOOK:
        #     pass
