from apps.device.serializers.input_serializer import DeviceCreateInputSerializer, DeviceUpdateInputSerializer
from apps.device.serializers.output_serializer import (
    DeviceListOutputSerializer,
    DeviceCreateOutputSerializer,
    DeviceUpdateOutputSerializer,
    DeviceByIDOutputSerializer,
    DeviceOutputDeleteSerializer,
    DeviceFirmwareOutupSerializer,
    DeviceGetCurrentVersionOutputSerializer
)
from apps.device.serializers.filter_serializer import DeviceFilterSerializer