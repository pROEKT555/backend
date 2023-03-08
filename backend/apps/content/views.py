from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Content, Tests, Question, Answer
from register.models import Register
from .serializer import *

class ContentView(APIView):
    def get(self, request):
        output = [{
                "author_id": output.author_id,
                "author_name": Register.objects.get(id=output.author_id).login,
                "name": output.name,
                "descript": output.descript,
                "files": output.files
            } for output in Content.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"complite": True})

class TestView(APIView):
    def get(self, request):
        test_output = [{
                "author_id": output.author_id,
                "author_name": Register.objects.get(id=output.author_id).login,
                "name": output.name
            } for output in Tests.objects.all()]
        question_output = [{
                "test_id": output.test_id,
                "text": output.text
            } for output in Question.objects.all()]
        answer_output = [{
            "question_id": output.question_id,
            "text": output.text,
            "is_true": output.is_true
        } for output in Answer.objects.all()]
        return Response({"test_output": test_output,
                         "question_output": question_output,
                         "answer_output": answer_output})

    def post(self, request):
        test_serializer = TestSerializer(data=request.data)

        if test_serializer.is_valid():
            obj = test_serializer.save()
        else:
            return Response(test_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"id": obj.id}, status=status.HTTP_201_CREATED)

class QuestionView(APIView):
    def post(self, request):
        question_serializer = QuestionSerializer(data=request.data)

        if question_serializer.is_valid():
            obj = question_serializer.save()
        else:
            return Response({"id": obj.id}, question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

class AnswerView(APIView):
    def post(self, request):
        answer_serializer = AnswerSerializer(data=request.data, many=True)

        if answer_serializer.is_valid():
            answer_serializer.save()
        else:
            return Response(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

"""
{
 "author": 1,
 "name": "zxcv"
}
{
 "test": 1,
 "text": "test"
}
[{
 "question": 1,
 "text": "калясік"
},
{
 "question": 1,
 "text": "дурень"
}]
"""
