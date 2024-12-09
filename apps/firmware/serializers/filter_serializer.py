from rest_framework import serializers

class FirmwareFilterSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    version = serializers.CharField(required=False)
    is_deleted = serializers.BooleanField(required=False)
