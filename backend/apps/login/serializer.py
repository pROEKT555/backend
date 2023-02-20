from rest_framework import serializers
from .models import Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['login', 'passworld', 'email']
