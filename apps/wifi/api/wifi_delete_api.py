# Imports do Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey

# Imports do drf-yasg (geração de documentação Swagger)
from drf_yasg.utils import swagger_auto_schema
from apps.core.exceptions import NotFoundError

# Imports relacionados à serialização e validação de dados
from apps.wifi.serializers import WifiOutputDeleteSerializer

# Imports de serviços
from apps.wifi.services import wifi_delete

class WifiDeleteApi(APIView):
    """Rota de exclusão de rede Wifi."""
    # permission_classes = [HasAPIKey]
    output_serializer = WifiOutputDeleteSerializer

    @swagger_auto_schema(
        tags=["Wifi"],
        operation_summary="Exclusão de rede Wifi",
        operation_description="Exclui uma rede Wifi pelo UUID",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def delete(self, request, uuid):
        wifi = wifi_delete(uuid=uuid)
        data = self.output_serializer(wifi).data
        return Response(status=status.HTTP_200_OK, data=data)
