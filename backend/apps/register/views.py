from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Register
from .serializer import RegisterSerializer

class RegisterView(APIView):
    def get(self, request):
        output = [{
                "login": output.login,
                "passworld": output.passworld,
                "email": output.email
            } for output in Register.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = Register.objects.all()
            obg = serializer.validated_data
            has_user = False

            for i in user:
                if (obg['login'] == i.login or
                     obg['email'] == i.email):
                    has_user = True
                    break

            if has_user == False:
                serializer.save()
            return Response({'has_user': has_user})
        else:
            return Response(serializer.errors, status=400)

class LoginView(APIView):    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = Register.objects.all()
            obg = serializer.validated_data
            has_user_found = False

            for i in user:
                if (obg['login'] == i.login or
                     obg['login'] == i.email):
                    has_user_found = True
                    break

            return Response({'has_user_found': has_user_found})
