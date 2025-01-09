
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticated

from apps.users.selectors import user_get_login_data

from apps.users.serializers.output_serializer import UserOutputSerializer as OutputSerializerUser

class UserMeApi(APIView):
    output_serializer = OutputSerializerUser
    permission_classes = [IsAuthenticated]
    
    """
        Rota para obter informações do usuário autenticado.

        Esta rota permite aos usuários autenticados obter informações sobre sua própria conta, como nome de usuário,
        email e outros detalhes relacionados.
    
    """
    @swagger_auto_schema(
        operation_summary='Obtenha informações do usuário autenticado.',
        operation_description='''Esta rota permite aos usuários autenticados obter informações sobre sua própria conta, como nome de usuário,email e outros detalhes relacionados.''',
        responses=None
    )

    def get(self, request):
        user = user_get_login_data(user=request.user)

        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = self.output_serializer(user).data
        
        return Response(data)