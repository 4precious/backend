from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    # content = serializers.CharField(max_length=150)

    class Meta:
        model = Question
        fields = ('id', 'user_email', 'content', 'created_at')


class AnswerSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    result_happiness = serializers.ReadOnlyField()
    result_anxiety = serializers.ReadOnlyField()
    result_embarrassment = serializers.ReadOnlyField()
    result_sadness = serializers.ReadOnlyField()
    result_anger = serializers.ReadOnlyField()
    result_injury = serializers.ReadOnlyField()

    class Meta:
        model = Answer
        fields = ('id', 'user_email', 'question', 'content', 'created_at', 'result_happiness', 'result_anxiety', 'result_embarrassment', 'result_sadness', 'result_anger', 'result_injury', 'result_max_sentiment')

class SentimentSerializer(serializers.ModelSerializer):
    # result_max_sentiment = serializers.ReadOnlyField()

    class Meta:
        model = Answer
        fields = ('result_max_sentiment',)
