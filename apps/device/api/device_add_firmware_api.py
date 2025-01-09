from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from apps.device.serializers import DeviceFirmwareOutputSerializer ,DeviceAddFirmwareInputSerializer
from apps.device.services import device_add_firmware

class DeviceAddFirmwareApi(APIView):

    permission_classes = [IsAuthenticated]

    input_serializer = DeviceAddFirmwareInputSerializer
    output_serializer = DeviceFirmwareOutputSerializer

    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Vincular Firmware em um device",
        operation_description="Vincular dispositivo em um device.",
        request_body=input_serializer,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        group = device_add_firmware(**serializer.validated_data)
        data = self.output_serializer(group).data
        return Response(status=status.HTTP_201_CREATED, data=data)