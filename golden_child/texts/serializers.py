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

    class Meta:
        model = Answer
        fields = ('id', 'user_email', 'question_id', 'content', 'created_at')
