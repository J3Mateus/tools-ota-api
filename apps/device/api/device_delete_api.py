from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.device.serializers import DeviceOutputDeleteSerializer
from apps.device.services import device_delete

class DeviceDeleteApi(APIView):
    output_serializer = DeviceOutputDeleteSerializer

    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Excluir um dispositivo",
        operation_description="Exclui um dispositivo pelo ID.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def delete(self, request, uuid):
        device = device_delete(id=uuid)
        data = self.output_serializer(device).data
        return Response(status=status.HTTP_200_OK, data=data)
