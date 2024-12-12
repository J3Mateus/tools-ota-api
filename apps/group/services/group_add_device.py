from apps.core.exceptions import NotFoundError
from apps.device.models.device import Device
from apps.group.models import Group
from django.db import transaction

from utils import get_object

@transaction.atomic
def group_add_device(*, device_id  : str, group_id : str) -> Group:
    """
    Adiciona um dispositivo a um grupo.

    Args:
        group_id (str): ID do grupo.
        device_id (str): ID do dispositivo.

    Returns:
        Group: A instância do grupo atualizada.
    """
    group = get_object(Group, uuid=group_id)

    if group is None:
        raise NotFoundError(extra={"group_id": group_id})
    
    device = get_object(Device, uuid=device_id)
    
    if device is None:
        raise NotFoundError(extra={"device_id": device_id})
    
    group.devices.add(device)
    
    return group