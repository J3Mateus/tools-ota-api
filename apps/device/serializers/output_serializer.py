from rest_framework import serializers

from apps.files.serializers.output_serializer import FileOutputListSerializer
from apps.firmware.serializers.output_serializer import FirmwareByIDOutputSerializer
from apps.users.serializers.output_serializer import UserApiKeyOutputSerializer
from apps.wifi.serializers.output_serializer import WifiByIDOutputSerializer
from apps.device.models import DeviceStatusBuild

class DeviceListOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        try:
            print(obj)
            return DeviceStatusBuild.objects.get(device=obj).status
        except DeviceStatusBuild.DoesNotExist:
            return None
        
class DeviceCreateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        try:
            return DeviceStatusBuild.objects.get(device=obj).status
        except DeviceStatusBuild.DoesNotExist:
            return None
        
class DeviceUpdateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        try:
            return DeviceStatusBuild.objects.get(device=obj).status
        except DeviceStatusBuild.DoesNotExist:
            return None
        
class DeviceByIDOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        try:
            return DeviceStatusBuild.objects.get(device=obj).status
        except DeviceStatusBuild.DoesNotExist:
            return None
        
class DeviceOutputDeleteSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        try:
            return DeviceStatusBuild.objects.get(device=obj).status
        except DeviceStatusBuild.DoesNotExist:
            return None
        
class DeviceFirmwareOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    code = serializers.CharField()
    firmware = serializers.UUIDField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        try:
            return DeviceStatusBuild.objects.get(device=obj).status
        except DeviceStatusBuild.DoesNotExist:
            return None
        
class DeviceFirmwareOutupSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    version = serializers.CharField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer()
    wifi     = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        try:
            print(obj)
            DeviceStatusBuild.objects.get(device=obj).status
        except DeviceStatusBuild.DoesNotExist:
            return None    
        
class DeviceGetCurrentVersionOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    version = serializers.CharField()
    device = DeviceByIDOutputSerializer()
    
class APIKeyOutputSerializer(serializers.Serializer):
    key = serializers.CharField()
    message = serializers.CharField()