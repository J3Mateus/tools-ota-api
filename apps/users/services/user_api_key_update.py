from typing import Dict, Tuple
from django.db import transaction
from apps.common.services.model_update import model_update
from apps.users.models import UserAPIKey

@transaction.atomic
def key_update(*, key: UserAPIKey, data: Dict[str, any]) -> Tuple[UserAPIKey, bool]:
    """
    Atualiza os dados de uma key.

    Args:
        key (UserAPIKey): Instância da key a ser atualizada.
        data (Dict[str, any]): Dados para atualização.

    Returns:
        Tuple[UserAPIKey, bool]: A instância atualizada e um booleano indicando se houve mudanças.
    """
    fields = ['name']

    new_key, has_updated, logs = model_update(instance=key, fields=fields, data=data)

    return new_key, has_updated
