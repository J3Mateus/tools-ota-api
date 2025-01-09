from rest_framework import serializers, status

class InputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()