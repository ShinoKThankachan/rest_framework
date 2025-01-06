from rest_framework import serializers
from .models import *


# class studserializer(serializers.Serializer):
#     name=serializers.CharField()
#     age=serializers.IntegerField()
#     email=serializers.CharField()

class studmodelserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'