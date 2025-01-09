# Imports do Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Imports relacionados ao Swagger
from drf_yasg.utils import swagger_auto_schema

# Imports dos Serializers e Services
from rest_framework.permissions import IsAuthenticated
from apps.users.selectors.user_get_login_data import user_get_login_data
from apps.users.services.user_create_api_key import user_create_api_key
from apps.users.serializers.output_serializer import UserApiKeyOutputSerializer
from apps.users.serializers.input_serializer import UserApiKeyInputSerializer

class UserCreateApiKeyApi(APIView):
    """Rota de criação de API key do usuário."""

    input_serializer = UserApiKeyInputSerializer
    output_serializer = UserApiKeyOutputSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["User"],
        operation_summary="Criar API key do usuário",
        operation_description="Cria uma nova API key para o usuário.",
        request_body=input_serializer,
        responses={status.HTTP_201_CREATED: output_serializer},
    )
    def post(self, request):

        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = user_get_login_data(user=request.user)

        api_key = user_create_api_key(**serializer.validated_data,user_id=user.id)
        data = self.output_serializer(api_key).data
        return Response(status=status.HTTP_201_CREATED, data=data)