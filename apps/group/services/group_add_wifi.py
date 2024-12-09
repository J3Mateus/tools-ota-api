from apps.core.exceptions import NotFoundError
from apps.wifi.models.wifi import Wifi
from apps.group.models import Group
from django.db import transaction

from utils import get_object

@transaction.atomic
def group_add_wifi(*,group_id:str,wifi_id: str) -> Group:
    """
    Adiciona um wifi a um grupo.

    Args:
        group_id (str): ID do grupo.
        wifi_id (str): ID do wifi.

    Returns:
        Group: A instância do grupo atualizada.
    """
    group = get_object(Group, uuid=group_id)

    if group is None:
        raise NotFoundError(extra={"group_id": group_id})
    
    wifi = get_object(Wifi, uuid=wifi_id)
    
    if wifi is None:
        raise NotFoundError(extra={"wifi_id": wifi_id})

    group.wifi = wifi
    group.full_clean()
    group.save()
    
    return group