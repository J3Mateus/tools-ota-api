from rest_framework import serializers

class KeyFilterSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(required=False)