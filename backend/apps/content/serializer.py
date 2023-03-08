from rest_framework import serializers
from .models import Content, Tests, Question, Answer
from register.serializer import RegisterSerializer

class ContentSerializer(serializers.ModelSerializer):
    author_id = RegisterSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    author_id = RegisterSerializer(many=True, read_only=True)

    class Meta:
        model = Tests
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    test_id = TestSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    question_id = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'
