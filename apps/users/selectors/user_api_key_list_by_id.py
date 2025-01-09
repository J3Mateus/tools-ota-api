from typing import Optional
from apps.users.models import UserAPIKey
from apps.core.exceptions import NotFoundError
from utils import get_object

def key_list_by_id(*, id: str) -> Optional[UserAPIKey]:
    """
    Busca uma key pelo ID.

    Args:
        id (str): ID da key.

    Returns:
        Optional[UserAPIKey]: A instância da key.

    Raises:
        NotFoundError: Se a key não for encontrado.
    """
    key = get_object(UserAPIKey, id=id)

    if key is None:
        raise NotFoundError(extra={"id": id})

    return key
