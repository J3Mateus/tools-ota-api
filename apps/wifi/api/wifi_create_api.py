# Imports do Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports relacionados ao Swagger
from drf_yasg.utils import swagger_auto_schema

# Imports dos Serializers e Services
from apps.wifi.serializers import WifiCreateInputSerializer, WifiCreateOutputSerializer
from apps.wifi.services import wifi_create


class WifiCreateApi(APIView):
    """Rota de criação de rede Wifi."""

    input_serializer = WifiCreateInputSerializer
    output_serializer = WifiCreateOutputSerializer
    # permission_classes = [HasAPIKey]

    @swagger_auto_schema(
        tags=["Wifi"],
        operation_summary="Criar uma rede Wifi",
        operation_description="Cria uma nova rede Wifi com SSDI e senha.",
        request_body=input_serializer,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        wifi = wifi_create(**serializer.validated_data)
        data = self.output_serializer(wifi).data
        return Response(status=status.HTTP_201_CREATED, data=data)
