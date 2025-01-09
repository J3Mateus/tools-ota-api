from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from apps.device.serializers import DeviceAddWifiInputSerializer, DeviceByIDOutputSerializer
from apps.device.services import device_add_wifi

from rest_framework.permissions import IsAuthenticated


class DeviceAddWifiApi(APIView):
    input_serializer = DeviceAddWifiInputSerializer
    output_serializer = DeviceByIDOutputSerializer

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Vincular wifi em um grupo",
        operation_description="Vincular wifi em um grupo.",
        request_body=input_serializer,
        responses={status.HTTP_201_CREATED: output_serializer},
        produces=["application/json"],
    )
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        device = device_add_wifi(**serializer.validated_data)
        data = self.output_serializer(device).data
        return Response(status=status.HTTP_201_CREATED, data=data)
