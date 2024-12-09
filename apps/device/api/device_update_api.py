from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.device.serializers import DeviceUpdateInputSerializer, DeviceUpdateOutputSerializer
from apps.device.services import device_update
from utils import get_object
from apps.core.exceptions import NotFoundError, UpdateError
from apps.device.models import Device

class DeviceUpdateApi(APIView):
    input_serializer = DeviceUpdateInputSerializer
    output_serializer = DeviceUpdateOutputSerializer

    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Atualizar um dispositivo",
        operation_description="Atualiza os dados de um dispositivo pelo ID.",
        request_body=input_serializer,
        responses={status.HTTP_202_ACCEPTED: output_serializer},
    )
    def patch(self, request, uuid):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        device = get_object(Device, uuid=uuid)
        if device is None:
            raise NotFoundError(extra={"id": uuid})
        new_device, updated = device_update(device=device, data=serializer.validated_data)
        if not updated:
            raise UpdateError(extra={"id": uuid}, status_code=status.HTTP_406_NOT_ACCEPTABLE)
        data = self.output_serializer(new_device).data
        return Response(status=status.HTTP_202_ACCEPTED, data=data)
