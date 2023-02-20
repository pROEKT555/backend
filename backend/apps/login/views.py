from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Login
from .serializer import LoginSerializer

class LoginView(APIView):
    def get(self, request):
        output = [{
                "login": output.login,
                "passworld": output.passworld,
                "email": output.email
            } for output in Login.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
