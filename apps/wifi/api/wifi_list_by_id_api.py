# Imports do Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports relacionados à autenticação da API
from rest_framework_api_key.permissions import HasAPIKey
# Imports relacionados ao Swagger
from drf_yasg.utils import swagger_auto_schema

# Imports dos Serializers e Services
from apps.wifi.selectors import wifi_list_by_id
from apps.wifi.serializers import WifiByIDOutputSerializer


class WifiByIDApi(APIView):
    """Rota para buscar uma rede Wifi pelo UUID."""
    output_serializer = WifiByIDOutputSerializer
    # permission_classes = [HasAPIKey]

    @swagger_auto_schema(
        request_body=None,
        responses=None,
        tags=["Wifi"],
        operation_summary="Buscar uma rede Wifi",
        operation_description="Buscar uma rede Wifi específica pelo UUID.",
        # responses={status.HTTP_200_OK: output_serializer},
    )
    def get(self, request, uuid):
        wifi = wifi_list_by_id(uuid=uuid)
        data = self.output_serializer(wifi).data
        return Response(status=status.HTTP_200_OK, data=data)
