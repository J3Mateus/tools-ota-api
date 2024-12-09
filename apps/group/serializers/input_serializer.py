from rest_framework import serializers

class GroupCreateInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class GroupUpdateInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)

class GroupAddFirmwareInputSerializer(serializers.Serializer):
    firmware_id = serializers.UUIDField()
    group_id = serializers.UUIDField()

class GroupAddDeviceInputSerializer(serializers.Serializer):
    device_id = serializers.UUIDField()
    group_id = serializers.UUIDField()

class GroupAddWifiInputSerializer(serializers.Serializer):
    wifi_id = serializers.UUIDField()
    group_id = serializers.UUIDField()
