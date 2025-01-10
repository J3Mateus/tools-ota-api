from rest_framework import serializers

from apps.files.serializers.output_serializer import FileOutputListSerializer
from apps.firmware.serializers.output_serializer import FirmwareByIDOutputSerializer
from apps.users.serializers.output_serializer import UserApiKeyOutputSerializer
from apps.wifi.serializers.output_serializer import WifiByIDOutputSerializer

class DeviceListOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)

class DeviceCreateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)

class DeviceUpdateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)

class DeviceByIDOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)

class DeviceOutputDeleteSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)

class DeviceFirmwareOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    firmware = serializers.UUIDField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)

class DeviceFirmwareOutupSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)
    
class DeviceGetCurrentVersionOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    version = serializers.CharField()
    device = DeviceByIDOutputSerializer()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)
    
class APIKeyOutputSerializer(serializers.Serializer):
    key = serializers.CharField()
    message = serializers.CharField()