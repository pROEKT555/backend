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
            serializer.save()
            return Response({"complite": True})
