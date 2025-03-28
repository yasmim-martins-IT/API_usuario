from .models import UserAbs
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta :
        model = UserAbs
        fields = '__all__'