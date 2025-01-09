from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema



class UserSessionLogoutApi(APIView):
    """
        Rota para realizar o logout e encerrar a sessão do usuário.

        Esta rota permite aos usuários encerrarem sua sessão ativa no sistema. Isso revoga o
        acesso autenticado e encerra a sessão do usuário.


        Utilize esta rota para encerrar a sessão ativa do usuário e efetuar o logout com segurança.
    """
    
    
    @swagger_auto_schema(
        operation_summary='Realize o logout e encerre a sessão do usuário.',
        operation_description="Utilize esta rota para encerrar a sessão ativa do usuário e efetuar o logout com segurança.",
        responses={200: "Sessão encerrada com sucesso."}
        )
    def post(self, request):
        logout(request)

        return Response()
    
    def get(self, request):
        logout(request)

        return Response()