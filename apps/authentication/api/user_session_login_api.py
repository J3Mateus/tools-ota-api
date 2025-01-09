from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from apps.authentication.serializers.input_serializer import InputSerializer

from apps.users.selectors import user_get_login_data




class UserSessionLoginApi(APIView):
    
    """
        Rota para realizar o login usando sessões de autenticação do Django.

        Esta rota permite aos usuários autenticarem-se no sistema usando o método de autenticação
        por sessão do Django. Ela segue o fluxo padrão de autenticação do Django e usa um serializer
        personalizado para validar os dados de entrada.

        Esta rota segue o método de autenticação padrão do Django e permite que os usuários iniciem uma sessão autenticada no sistema. Certifique-se de fornecer as credenciais corretas para autenticar com sucesso.
    """
    
    input_Serializer = InputSerializer
    @swagger_auto_schema(
        operation_summary='Realize o login usando sessões de autenticação do Django.',
        operation_description='''Rota para realizar o login usando sessões de autenticação do Django.
      
        #Usuario padrão
        email:admin@admin.com
        password:admin
        
        
        Esta rota permite aos usuários autenticarem-se no sistema usando o método de autenticação
        por sessão do Django. Ela segue o fluxo padrão de autenticação do Django e usa um serializer
        personalizado para validar os dados de entrada.''',
        request_body=None,
        responses=None
    )
    def post(self, request):
        serializer = self.input_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.validated_data)

        if user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        data = user_get_login_data(user=user)
        session_key = request.session.session_key

        return Response({"session": session_key, "data": data})
