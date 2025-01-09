from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.authentication.selector import get_user_from_access_token_in_django_rest_framework_simplejwt

class UserJwtLoginApi(TokenObtainPairView):
    
    """
        Rota para realizar o login usando JWT (JSON Web Token).

        Esta rota permite aos usuários autenticarem-se no sistema e obter um token JWT válido
        para acessar recursos protegidos.
    """


    @swagger_auto_schema(
        operation_summary='Realize o login usando JWT (JSON Web Token).',
        request_body=None,
        operation_description='''Esta rota permite aos usuários autenticarem-se no sistema e obter um token JWT válido para acessar recursos protegidos.
        
        #Usuario padrão
        email:admin@admin.com
        password:admin
        ''',    
        responses=None
        )  
    def post(self, request, *args, **kwargs):
        # We are redefining post so we can change the response status on success
        # Mostly for consistency with the session-based API
        response = super().post(request, *args, **kwargs)  
        
        user = get_user_from_access_token_in_django_rest_framework_simplejwt(response.data.get("access"))
        
        if user.is_deleted:
            return Response(status=status.HTTP_401_UNAUTHORIZED,data={
                            "message": "Este usuário foi desativado.",
                            "extra": {}
                            })
        
        if response.status_code == status.HTTP_201_CREATED:
            response.status_code = status.HTTP_200_OK

        return response