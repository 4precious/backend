from rest_framework import serializers
from .models import parent_question, child_answer

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = parent_question
        fields = ('id', 'user', 'content', 'create_date')
    
class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = child_answer
        fields = ('user','question', 'content', 'create_date')