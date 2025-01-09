from typing import Dict, Tuple
from django.db import transaction
from apps.common.services.model_update import model_update
from apps.group.models import Group

@transaction.atomic
def group_update(*, group: Group, data: Dict[str, any]) -> Tuple[Group, bool]:
    """
    Atualiza os dados de um grupo.

    Args:
        group (Group): Instância do grupo a ser atualizada.
        data (Dict[str, any]): Dados para atualização.

    Returns:
        Tuple[Group, bool]: A instância atualizada e um booleano indicando se houve mudanças.
    """
    fields = ['name']

    new_group, has_updated, logs = model_update(instance=group, fields=fields, data=data)

    return new_group, has_updated
