from rest_framework import serializers
from .models import parent_question, child_answer

class QuestionSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = parent_question
        fields = ('id', 'user_id', 'content', 'create_date')
    
class AnswerSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = child_answer
        fields = ('user_id','question', 'content', 'create_date')