from rest_framework import serializers
from .models import Content
from register.serializer import RegisterSerializer

class ContentSerializer(serializers.ModelSerializer):
    author_id = RegisterSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = '__all__'
