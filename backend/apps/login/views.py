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
            user = Login.objects.all()
            obg = serializer.validated_data
            has_user = False
            
            for i in user:
                if (obg['login'] == i.login or
                     obg['email'] == i.email):
                    has_user = True
                    break
            
            if has_user == False:
                serializer.save()
            send_inf = {'has_user': has_user}
            return Response(send_inf)
        else:
            return Response(serializer.errors, status=400)
