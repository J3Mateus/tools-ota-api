from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.device.serializers import DeviceOutputDeleteSerializer
from apps.device.services import device_undelete
from rest_framework.permissions import IsAuthenticated


class DeviceUnDeleteApi(APIView):
    output_serializer = DeviceOutputDeleteSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Ativa um dispositivo",
        operation_description="Ativa um dispositivo pelo ID.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def delete(self, request, uuid):
        device = device_undelete(id=uuid)
        data = self.output_serializer(device).data
        return Response(status=status.HTTP_200_OK, data=data)
