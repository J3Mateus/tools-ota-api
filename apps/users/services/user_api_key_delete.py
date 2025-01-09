from typing import Optional
from apps.users.models import UserAPIKey
from apps.core.exceptions import NotFoundError
from apps.users.models import BaseUser
from utils import get_object

def key_delete(*, uuid: str,user: BaseUser) -> UserAPIKey:
    """
    Deleta uma api key pelo UUID.

    Args:
        uuid (str): UUID da key.

    Returns:
        Key: A key que foi deletada.

    Raises:
        NotFoundError: Se a key não for encontrada.
    """
    key: Optional[UserAPIKey] = get_object(UserAPIKey, id=uuid)

    if key is None:
        raise NotFoundError(extra={"uuid": uuid})

    key.revoke()
    key.delete(user)
    return key
