from typing import Optional
from apps.group.models import Group
from apps.core.exceptions import NotFoundError
from utils import get_object

def group_delete(*, uuid: str) -> Group:
    """
    Deleta um grupo pelo UUID.

    Args:
        uuid (str): UUID do grupo.

    Returns:
        Group: O grupo deletado.

    Raises:
        NotFoundError: Se o grupo não for encontrado.
    """
    group: Optional[Group] = get_object(Group, uuid=uuid)

    if group is None:
        raise NotFoundError(extra={"uuid": uuid})

    group.delete()
    return group
