from rest_framework import serializers

class WifiFilterSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(required=False)
    SSDI = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
