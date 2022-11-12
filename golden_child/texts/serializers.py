from rest_framework import serializers
from .models import parent_question, child_answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = parent_question
        fields = ('id', 'content', 'create_date')
    
class AnswerSerializer(serializers.ModelSerializer):
    #question = QuestionSerializer(read_only = True)
    class Meta:
        model = child_answer
        fields = ('question', 'content', 'create_date')