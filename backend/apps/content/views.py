from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Content
from register.models import Register
from .serializer import ContentSerializer

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
            # user = Content.objects.all()
            # obg = serializer.validated_data
            # has_user = False

            # for i in user:
            #     if (obg['login'] == i.login or
            #          obg['email'] == i.email):
            #         has_user = True
            #         break

            # if has_user == False:
            serializer.save()
            return Response({"complite": True})
