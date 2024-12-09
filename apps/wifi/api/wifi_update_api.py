# Imports do Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports relacionados à autenticação da API
from rest_framework_api_key.permissions import HasAPIKey

# Imports do drf-yasg (geração de documentação Swagger)
from drf_yasg.utils import swagger_auto_schema

# Imports de exceptions
from apps.core.exceptions import NotFoundError, UpdateError

# Imports de models
from apps.wifi.models import Wifi

from apps.wifi.serializers import WifiUpdateInputSerializer, WifiUpdateOutputSerializer
from apps.wifi.services import wifi_update
from utils import get_object

class WifiUpdateApi(APIView):
    input_serializer = WifiUpdateInputSerializer
    output_serializer = WifiUpdateOutputSerializer
    # permission_classes = [HasAPIKey]

    @swagger_auto_schema(
        tags=["Wifi"],
        operation_summary="Atualizar uma rede Wifi",
        operation_description="Atualizar dados de uma rede Wifi existente pelo UUID.",
        request_body=input_serializer,
        responses={status.HTTP_202_ACCEPTED: output_serializer},
    )
    def patch(self, request, uuid):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        wifi = get_object(Wifi, uuid=uuid)
        if wifi is None:
            raise NotFoundError(extra={
                "uuid": uuid
            })

        new_wifi, updated = wifi_update(wifi=wifi, data=serializer.validated_data)
        if not updated:
            raise UpdateError(extra={
                "uuid": uuid
            }, status_code=status.HTTP_406_NOT_ACCEPTABLE)

        data = self.output_serializer(new_wifi).data
        return Response(status=status.HTTP_202_ACCEPTED, data=data)
