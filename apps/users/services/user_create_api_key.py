from apps.core.exceptions import NotFoundError
from apps.users.models import BaseUser, UserAPIKey
from django.db import transaction

from utils import get_object

@transaction.atomic
def user_create_api_key(*,name: str, user_id: int) -> BaseUser:
    """
    Cria uma nova API key para o usuário.

    Args:
        user_id (int): ID do usuário.

    Returns:
        User : A instância criada da API key do usuário.
    """

    user = get_object(BaseUser, id=user_id)

    if not user:
        raise NotFoundError(extra={
            "uuid": user_id
        })

    user_api_key = UserAPIKey.create_key(user,name)
    return user_api_key