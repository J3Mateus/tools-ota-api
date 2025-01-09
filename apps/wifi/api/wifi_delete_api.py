# Imports do Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Imports do drf-yasg (geração de documentação Swagger)
from drf_yasg.utils import swagger_auto_schema
from apps.api.mixins import ApiAuthMixin

# Imports relacionados à serialização e validação de dados
from apps.users.selectors import user_get_login_data
from apps.wifi.serializers import WifiOutputDeleteSerializer

# Imports de serviços
from apps.wifi.services import wifi_delete

class WifiDeleteApi(APIView):
    """Rota de exclusão de rede Wifi."""
    permission_classes = [IsAuthenticated]
    output_serializer = WifiOutputDeleteSerializer

    @swagger_auto_schema(
        tags=["Wifi"],
        operation_summary="Exclusão de rede Wifi",
        operation_description="Exclui uma rede Wifi pelo UUID",
        responses={status.HTTP_200_OK: output_serializer},
    )
    def delete(self, request, uuid):
        user = user_get_login_data(user=request.user)
        
        wifi = wifi_delete(uuid=uuid,user=user)
        data = self.output_serializer(wifi).data
        return Response(status=status.HTTP_200_OK, data=data)
