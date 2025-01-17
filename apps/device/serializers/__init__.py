from apps.device.serializers.input_serializer import (
    DeviceCreateInputSerializer,
    DeviceUpdateInputSerializer,
    DeviceAPIKeyCreateInputSerializer,
    DeviceAddFirmwareInputSerializer,
    DeviceAddWifiInputSerializer,
    DeviceStatusBuildInputSerializer
)

from apps.device.serializers.output_serializer import (
    DeviceListOutputSerializer,
    DeviceCreateOutputSerializer,
    DeviceUpdateOutputSerializer,
    DeviceByIDOutputSerializer,
    DeviceOutputDeleteSerializer,
    DeviceFirmwareOutupSerializer,
    DeviceGetCurrentVersionOutputSerializer,
    DeviceFirmwareOutputSerializer,
    APIKeyOutputSerializer
)
from apps.device.serializers.filter_serializer import DeviceFilterSerializer