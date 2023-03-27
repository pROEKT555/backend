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
            "question_id": output.id,
            "test_id": output.test_id,
            "quzitrue": output.quzitrue,
            "text": output.text,
            "answer": [{
                "question_id": answ.question_id,
                "text": answ.text
            } for answ in Answer.objects.filter(question_id=output.id)]
        } for output in Question.objects.all()]
        return Response({"test_output": test_output,
                         "question_output": question_output})

    def post(self, request):
        test_serializer = TestSerializer(data=request.data[0])

        if test_serializer.is_valid():
            obj_test = test_serializer.save()
            request.data.pop(0)
        else:
            return Response(test_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        for i in range(len(request.data)):
            request.data[i]["test"] = int(obj_test.id)
            question_complit_data = {"test": request.data[i]["test"],
                                     "text": request.data[i]["text"],
                                     "quzitrue": request.data[i]["quzitrue"]}
            question_serializer = QuestionSerializer(data=question_complit_data)

            if question_serializer.is_valid():
                obj_question = question_serializer.save()
            else:
                return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            for j in range(len(request.data[i]["answ"])):
                request.data[i]["answ"][j]["question"] = int(obj_question.id)
            answer_serializer = AnswerSerializer(data=request.data[i]["answ"], many=True)

            if answer_serializer.is_valid():
                answer_serializer.save()
            else:
                return Response(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)
