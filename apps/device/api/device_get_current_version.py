from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from apps.core.permission.api_key_permission import APIKeyPermission
from apps.device.selectors import device_get_current_version
from apps.device.serializers.output_serializer import DeviceGetCurrentVersionOutputSerializer

class DeviceGetCurrentVersionApi(APIView):
    output_serializer = DeviceGetCurrentVersionOutputSerializer
    permission_classes = [APIKeyPermission]
    
    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Obter a versão atual do firmware",
        operation_description="Obtém informações sobre a versão atual do firmware de um dispositivo.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def get(self, request, device_id):
        device = device_get_current_version(device_id=device_id)
        serializer = self.output_serializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)