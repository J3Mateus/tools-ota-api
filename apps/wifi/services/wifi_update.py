from typing import Dict, Tuple
from django.db import transaction
from apps.common.services.model_update import model_update
from apps.wifi.models import Wifi

@transaction.atomic
def wifi_update(*, wifi: Wifi, data: Dict[str, any]) -> Tuple[Wifi, bool]:
    """
    Atualiza uma instância de Wifi.
    
    Args:
        wifi (Wifi): A instância do modelo Wifi a ser atualizada.
        data (Dict[str, any]): Um dicionário contendo os dados a serem atualizados.
    
    Returns:
        Tuple[Wifi, bool]: A instância atualizada e um booleano indicando se houve mudanças.
    """
    fields = ['SSDI', 'password']

    new_wifi, has_updated,logs = model_update(instance=wifi, fields=fields, data=data)

    return new_wifi, has_updated
