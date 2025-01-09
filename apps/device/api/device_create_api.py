from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.core.permission.api_key_permission import APIKeyPermission
from apps.device.serializers import DeviceCreateInputSerializer, DeviceCreateOutputSerializer
from apps.device.services import device_create
from apps.users.models import UserAPIKey


class DeviceCreateApi(APIView):
    input_serializer = DeviceCreateInputSerializer
    output_serializer = DeviceCreateOutputSerializer
    permission_classes = [APIKeyPermission]
    
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
        api_key = request.headers.get('X-API-KEY')

        # Verifica se veio algum valor no cabeçalho
        if not api_key:
            return False   
        
        api_key = UserAPIKey.objects.filter(key=api_key, is_deleted=False).first()          
        device = device_create(**serializer.validated_data,user=api_key.user)
        data = self.output_serializer(device).data
        return Response(status=status.HTTP_201_CREATED, data=data)
