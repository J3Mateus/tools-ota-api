from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from apps.core.permission.api_key_permission import APIKeyPermission
from apps.device.selectors import device_get_firmware
from apps.firmware.serializers.output_serializer import FirmwareByDeviceIDOutputSerializer
from rest_framework.permissions import IsAuthenticated

class DeviceGetFirmwareApi(APIView):
    output_serializer = FirmwareByDeviceIDOutputSerializer
    # permission_classes = [IsAuthenticated | APIKeyPermsion]
    permission_classes = [APIKeyPermission]
    
    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Obter firmware",
        operation_description="Obtém informações sobre o firmware de um dispositivo.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def get(self, request, device_id):
        device = device_get_firmware(device_id=device_id)
        serializer = self.output_serializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)