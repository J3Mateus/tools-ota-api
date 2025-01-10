from typing import Optional
from apps.group.models import Group
from apps.core.exceptions import NotFoundError
from utils import get_object

def group_list_by_id(*, uuid: str) -> Optional[Group]:
    """
    Busca um grupo pelo UUID.

    Args:
        uuid (str): UUID do grupo.

    Returns:
        Optional[Group]: A instância do grupo.

    Raises:
        NotFoundError: Se o grupo não for encontrado.
    """
    group = get_object(Group, uuid=uuid)

    print(group.api_key)
    if group is None:
        raise NotFoundError(extra={"uuid": uuid})

    return group
