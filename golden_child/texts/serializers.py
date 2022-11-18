from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Question
        fields = ('id', 'user_id', 'content', 'created_at')


class AnswerSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Answer
        fields = ('user_id', 'question', 'content', 'created_at')
