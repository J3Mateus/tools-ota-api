from rest_framework import serializers

from apps.device.models.device_status_build import DeviceStatusBuild

class DeviceCreateInputSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255)

class DeviceUpdateInputSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255, required=False)

class DeviceAPIKeyCreateInputSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255)

class DeviceAddFirmwareInputSerializer(serializers.Serializer):
    firmware_id = serializers.UUIDField()
    device_id = serializers.UUIDField()

class DeviceAddWifiInputSerializer(serializers.Serializer):
    wifi_id = serializers.UUIDField()
    device_id = serializers.UUIDField()


class DeviceStatusBuildInputSerializer(serializers.Serializer):
    device_code = serializers.CharField()
    status = serializers.ChoiceField(choices=[ tag for tag in ['in_build', 'completed_build']])