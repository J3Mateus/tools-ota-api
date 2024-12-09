from apps.group.models import Group
from django.db import transaction

@transaction.atomic
def group_create(*, name: str, active: bool = True) -> Group:
    """
    Cria um novo grupo.

    Args:
        name (str): Nome do grupo.
        active (bool): Indica se o grupo está ativo (padrão: True).

    Returns:
        Group: A instância criada do grupo.
    """
    instance_group = Group(
        name=name,
        active=active
    )
    instance_group.save()
    return instance_group
