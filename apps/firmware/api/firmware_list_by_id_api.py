from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from apps.firmware.serializers.output_serializer import FirmwareByIDOutputSerializer
from apps.firmware.selectors import firmware_list_by_id
from rest_framework.permissions import IsAuthenticated

class FirmwareByIDApi(APIView):
    """
    API para buscar um firmware pelo UUID.
    """
    output_serializer = FirmwareByIDOutputSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Firmware"],
        operation_summary="Buscar um firmware",
        operation_description="Busca um firmware específico pelo UUID.",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def get(self, request, uuid):
        firmware = firmware_list_by_id(uuid=uuid)
        data = self.output_serializer(firmware).data
        return Response(status=status.HTTP_200_OK, data=data)
