from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.firmware.serializers.input_serializer import FirmwareUpdateInputSerializer
from apps.firmware.serializers.output_serializer import FirmwareUpdateOutputSerializer
from apps.firmware.services import firmware_update
from utils import get_object
from apps.core.exceptions import NotFoundError, UpdateError
from apps.firmware.models import Firmware

class FirmwareUpdateApi(APIView):
    """
    API para atualizar os dados de um firmware.
    """
    input_serializer = FirmwareUpdateInputSerializer
    output_serializer = FirmwareUpdateOutputSerializer

    @swagger_auto_schema(
        tags=["Firmware"],
        operation_summary="Atualizar um firmware",
        operation_description="Atualiza os dados de um firmware pelo UUID.",
        request_body=input_serializer,
    )
    def patch(self, request, uuid):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        firmware = get_object(Firmware, uuid=uuid)
        if firmware is None:
            raise NotFoundError(extra={"uuid": uuid})
        new_firmware, updated = firmware_update(firmware=firmware, data=serializer.validated_data)
        if not updated:
            raise UpdateError(extra={"uuid": uuid}, status_code=status.HTTP_406_NOT_ACCEPTABLE)
        data = self.output_serializer(new_firmware).data
        return Response(status=status.HTTP_202_ACCEPTED, data=data)
