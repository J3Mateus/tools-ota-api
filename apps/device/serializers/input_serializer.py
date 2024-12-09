from rest_framework import serializers

class DeviceCreateInputSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255)

class DeviceUpdateInputSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255, required=False)