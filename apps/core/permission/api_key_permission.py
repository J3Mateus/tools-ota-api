from rest_framework.permissions import BasePermission
from apps.users.models import UserAPIKey
from uuid import UUID

class APIKeyPermission(BasePermission):
    """
    Permite o acesso somente se o cabeçalho 'X-API-KEY' 
    for fornecido, for um UUID válido e corresponder a uma chave 
    existente no banco (is_deleted=False).
    """
    message = "API Key inválida ou não fornecida."

    def has_permission(self, request, view):
        api_key = request.headers.get('X-API-KEY')

        # Verifica se veio algum valor no cabeçalho
        if not api_key:
            return False

        # Tenta validar se a string é um UUID (versão 4, por exemplo)
        try:
            UUID(api_key, version=4)
        except ValueError:
            # Caso não seja um UUID válido, retorna False
            return False

        # Verifica se a chave existe no banco de dados e não está marcada como deletada
        user_api_key_exists = UserAPIKey.objects.filter(key=api_key, is_deleted=False).exists()
        
        return user_api_key_exists
