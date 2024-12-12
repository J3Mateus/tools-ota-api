from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from apps.device.services import device_update_version_current
from apps.device.serializers.output_serializer import DeviceGetCurrentVersionOutputSerializer

class DeviceUpdateVersionCurrentApi(APIView):
    output_serializer = DeviceGetCurrentVersionOutputSerializer

    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Insere qual é a versão que está rodando atualmente no device",
        operation_description="Vincula a versão que está rodando atualmente no device.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def post(self, request, device_id,firmware_id):
        device = device_update_version_current(device_id=device_id,firmware_id=firmware_id)
        serializer = self.output_serializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)