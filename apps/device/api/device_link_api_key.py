# Imports do Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports relacionados ao Swagger
from drf_yasg.utils import swagger_auto_schema

# Imports dos Serializers e Services
from rest_framework.permissions import IsAuthenticated
from apps.device.services.device_link_api_key import device_link_api_key

from apps.device.serializers.output_serializer import DeviceByIDOutputSerializer

class DeviceLinkApiKeyApi(APIView):
    """Rota de criação de API key do usuário."""

    output_serializer = DeviceByIDOutputSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Device"],
        operation_summary="Vincular apikey ao device",
        operation_description="Vincula uma nova API key ao device.",
        request_body=None,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def post(self, request , device_uuid , api_key_uuid):
        
        device = device_link_api_key(device_uuid=device_uuid,api_key_uuid=api_key_uuid)

        data = self.output_serializer(device).data
        return Response(status=status.HTTP_201_CREATED, data=data)