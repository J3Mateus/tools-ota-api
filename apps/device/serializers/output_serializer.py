from rest_framework import serializers

from apps.files.serializers.output_serializer import FileOutputListSerializer
from apps.firmware.serializers.output_serializer import FirmwareByIDOutputSerializer

class DeviceListOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()

class DeviceCreateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()

class DeviceUpdateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()

class DeviceByIDOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()

class DeviceOutputDeleteSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()

class DeviceFirmwareOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    firmware = serializers.UUIDField()
    is_deleted = serializers.BooleanField()

class DeviceFirmwareOutupSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    link_bin = serializers.URLField(allow_null=True)
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()

class DeviceGetCurrentVersionOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    version = serializers.CharField()
    device = DeviceByIDOutputSerializer()