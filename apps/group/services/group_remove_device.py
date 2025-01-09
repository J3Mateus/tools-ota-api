from apps.core.exceptions import NotFoundError
from apps.device.models.device import Device
from apps.group.models import Group
from django.db import transaction

from utils import get_object

@transaction.atomic
def group_remove_device(*, device_id: str, group_id: str) -> Group:
    """
    Remove um dispositivo de um grupo.

    Args:
        group_id (str): ID do grupo.
        device_id (str): ID do dispositivo.

    Returns:
        Group: A instância do grupo atualizada.
    """
    # Busca o grupo
    group = get_object(Group, uuid=group_id)
    if group is None:
        raise NotFoundError(extra={"group_id": group_id})

    # Busca o dispositivo
    device = get_object(Device, uuid=device_id)
    if device is None:
        raise NotFoundError(extra={"device_id": device_id})

    # Remove o dispositivo do grupo
    group.devices.remove(device)

    return group
