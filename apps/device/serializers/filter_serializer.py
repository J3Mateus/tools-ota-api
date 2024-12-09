from rest_framework import serializers

class DeviceFilterSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(required=False)
    code = serializers.CharField(required=False)
