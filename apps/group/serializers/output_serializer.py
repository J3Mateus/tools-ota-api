from rest_framework import serializers

from apps.device.serializers.output_serializer import DeviceByIDOutputSerializer
from apps.firmware.serializers.output_serializer import FirmwareByIDOutputSerializer
from apps.group.models import Group
from apps.users.serializers.output_serializer import UserApiKeyOutputSerializer
from apps.wifi.serializers.output_serializer import WifiByIDOutputSerializer

class GroupListOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    active = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer(allow_null=True)
    device = serializers.SerializerMethodField()
    wifi   = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)
    
    def get_device(self, obj: Group):
        devices = obj.devices.all()
        return DeviceByIDOutputSerializer(devices,many=True).data
    
class GroupCreateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    active = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer(allow_null=True)
    device = serializers.SerializerMethodField()
    wifi   = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)

    def get_device(self, obj: Group):
        devices = obj.devices.all()
        return DeviceByIDOutputSerializer(devices,many=True).data
    
class GroupUpdateOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    active = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer(allow_null=True)
    device = serializers.SerializerMethodField()
    Wifi   = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)

    def get_device(self, obj: Group):
        devices = obj.devices.all()
        return DeviceByIDOutputSerializer(devices,many=True).data
    
class GroupByIDOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    active = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer(allow_null=True)
    device = serializers.SerializerMethodField()
    wifi   = WifiByIDOutputSerializer()
    api_key = UserApiKeyOutputSerializer(allow_null=True)

    def get_device(self, obj: Group):
        devices = obj.devices.all()
        return DeviceByIDOutputSerializer(devices,many=True).data
    
class GroupOutputDeleteSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    active = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer(allow_null=True)
    device = serializers.SerializerMethodField()
    wifi   = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)    

    def get_device(self, obj: Group):
        devices = obj.devices.all()
        return DeviceByIDOutputSerializer(devices,many=True).data
    

class GroupAddFirmwareOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    active = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer(allow_null=True)
    device = serializers.SerializerMethodField()
    wifi   = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)    

    def get_device(self, obj: Group):
        devices = obj.devices.all()
        return DeviceByIDOutputSerializer(devices,many=True).data
    
class GroupAddDeviceOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    active = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer(allow_null=True)
    device = serializers.SerializerMethodField()
    wifi   = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)

    def get_device(self, obj: Group):
        devices = obj.devices.all()
        return DeviceByIDOutputSerializer(devices,many=True).data

class GroupAddWifiOutputSerializer(serializers.Serializer):

    uuid = serializers.UUIDField()
    name = serializers.CharField()
    active = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer(allow_null=True)
    device = serializers.SerializerMethodField()
    wifi   = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)
        
    def get_device(self, obj: Group):
        devices = obj.devices.all()
        return DeviceByIDOutputSerializer(devices,many=True).data

class GroupRemoveDeviceOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    active = serializers.BooleanField()
    firmware = FirmwareByIDOutputSerializer(allow_null=True)
    device = serializers.SerializerMethodField()
    wifi   = WifiByIDOutputSerializer(allow_null=True)
    api_key = UserApiKeyOutputSerializer(allow_null=True)

    def get_device(self, obj: Group):
        devices = obj.devices.all()
        return DeviceByIDOutputSerializer(devices,many=True).data