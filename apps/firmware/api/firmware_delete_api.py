from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.firmware.serializers.output_serializer import FirmwareOutputDeleteSerializer
from apps.firmware.services import firmware_delete

class FirmwareDeleteApi(APIView):
    """
    API para deletar um firmware pelo UUID.
    """
    output_serializer = FirmwareOutputDeleteSerializer

    @swagger_auto_schema(
        tags=["Firmware"],
        operation_summary="Deletar um firmware",
        operation_description="Deleta um firmware pelo UUID.",
        responses={status.HTTP_200_OK: output_serializer},
        
    )
    def delete(self, request, uuid):
        firmware = firmware_delete(uuid=uuid)
        data = self.output_serializer(firmware).data
        return Response(status=status.HTTP_200_OK, data=data)
