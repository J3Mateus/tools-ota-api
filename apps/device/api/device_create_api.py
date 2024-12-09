from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.device.serializers import DeviceCreateInputSerializer, DeviceCreateOutputSerializer
from apps.device.services import device_create

class DeviceCreateApi(APIView):
    input_serializer = DeviceCreateInputSerializer
    output_serializer = DeviceCreateOutputSerializer

    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Criar um dispositivo",
        operation_description="Cria um novo dispositivo.",
        request_body=input_serializer,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        device = device_create(**serializer.validated_data)
        data = self.output_serializer(device).data
        return Response(status=status.HTTP_201_CREATED, data=data)
