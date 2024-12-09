from rest_framework import serializers

class FirmwareCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    version = serializers.CharField(max_length=50)
    code = serializers.CharField(required=False, allow_null=True)
    link_bin = serializers.URLField(required=False, allow_null=True)

class FirmwareUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False)
    version = serializers.CharField(max_length=50, required=False)
    code = serializers.CharField(required=False, allow_null=True)
    link_bin = serializers.URLField(required=False, allow_null=True)