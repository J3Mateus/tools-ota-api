from apps.firmware.serializers.input_serializer import FirmwareCreateInputSerializer, FirmwareUpdateInputSerializer
from apps.firmware.serializers.output_serializer import (
    FirmwareListOutputSerializer,
    FirmwareCreateOutputSerializer,
    FirmwareUpdateOutputSerializer,
    FirmwareByIDOutputSerializer,
    FirmwareOutputDeleteSerializer,
    FirmwareByDeviceIDOutputSerializer
)
from apps.firmware.serializers.filter_serializer import FirmwareFilterSerializer