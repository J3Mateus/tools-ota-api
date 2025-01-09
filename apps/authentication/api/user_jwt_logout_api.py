from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticated
from apps.authentication.services import auth_logout


class UserJwtLogoutApi(APIView):
    """
        Rota para realizar o logout e revogar tokens JWT de um usuário autenticado.

        Esta rota permite aos usuários encerrarem sua sessão ativa no sistema e revogarem os tokens
        JWT associados à sua autenticação.
    
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Realize o logout e revogue os tokens JWT de um usuário autenticado.',
        operation_description='''Esta rota permite aos usuários encerrarem sua sessão ativa no sistema e revogarem os tokens JWT associados à sua autenticação.''',
        request_body=None,
        responses=None
    )
    
    def post(self, request):
 
        auth_logout(request.user,request.data.get("refresh"))
        response = Response()

        return response