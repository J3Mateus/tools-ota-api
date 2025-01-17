from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.device.serializers import DeviceByIDOutputSerializer
from apps.device.services import device_remove_firmware
from rest_framework.permissions import IsAuthenticated

class DeviceRemoveFirmwareApi(APIView):
    output_serializer = DeviceByIDOutputSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Remove a versão de firmware de um dispostivo",
        operation_description="Remove a versão de firmware de um dispostivo em especifico.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def post(self, request, uuid):
        device = device_remove_firmware(device_uuid=uuid)
        data = self.output_serializer(device).data
        return Response(status=status.HTTP_200_OK, data=data)
