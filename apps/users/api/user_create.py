
# Imports do Django REST framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Imports do drf-yasg (geração de documentação Swagger)
from drf_yasg.utils import swagger_auto_schema

# Imports de serializadores de usuários
from apps.users.serializers.output_serializer import UserOutputSerializer
from apps.users.serializers.input_serializer import UserCreateInputSerializer

# Imports relacionados aos usuários
from apps.users.selectors import get_user_by_email
from apps.users.services import user_create

class UserCreateApi(APIView):

    input_serializer = UserCreateInputSerializer
    output_serializer = UserOutputSerializer
    @swagger_auto_schema(
        tags=["User"],
        operation_summary="Criar um Usuário",
        operation_description="Esta rota permite a criação de um novo usuário com os dados fornecidos. O usuário não deve existir previamente no banco de dados. Se o email fornecido já estiver em uso, a criação falhará.",
        request_body=input_serializer,
    )
    def post(self, request):
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        verify_user = get_user_by_email(email=email)
        
        if verify_user :
            return Response(status=status.HTTP_409_CONFLICT,data={
                "message":{"detail": "A chave única já existe no banco de dados."},
                "code": "Conflict",
                "messages": [
                    {
                        "field": "email",
                        "message": "O email já está sendo usado por um usuario"
                    }
                ],
                "extra": {}
                })
        
        user = user_create(**serializer.validated_data,created_by=request.user)
        data = self.output_serializer(user).data
        return Response(status=status.HTTP_201_CREATED,data=data)