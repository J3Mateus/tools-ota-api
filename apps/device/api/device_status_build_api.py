from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.device.serializers import DeviceByIDOutputSerializer, DeviceStatusBuildInputSerializer
from apps.device.services import device_status_build
from rest_framework.permissions import IsAuthenticated
from apps.core.permission.api_key_permission import APIKeyPermission
from rest_framework_api_key.permissions import HasAPIKey

class DeviceStatusBuildApi(APIView):

    input_serializer = DeviceStatusBuildInputSerializer
    output_serializer = DeviceByIDOutputSerializer
    permission_classes = [IsAuthenticated | APIKeyPermission | HasAPIKey ]
    
    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Atualiza o status de build do device",
        operation_description="Atualiza o status de build do device em especifico.",
        request_body=input_serializer,
        responses={status.HTTP_200_OK: output_serializer},
    )
    def post(self, request):

        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        device = device_status_build(**serializer.validated_data)
        data = self.output_serializer(device).data
        return Response(status=status.HTTP_200_OK, data=data)
