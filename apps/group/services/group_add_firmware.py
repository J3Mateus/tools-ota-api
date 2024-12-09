from apps.core.exceptions import NotFoundError
from apps.device.models.device_version import DeviceVersion
from apps.firmware.models.firmware import Firmware
from apps.group.models import Group
from django.db import transaction

from utils import get_object

@transaction.atomic
def group_add_firmware(*,group_id: str, firmware_id: str) -> Group:
    """
    Adiciona um firmware a um grupo.

    Args:
        group_id (str): ID do grupo.
        firmware_id (str): ID do firmware.

    Returns:
        Group: A instância do grupo atualizada.
    """
    group = get_object(Group, uuid=group_id)

    if group is None:
        raise NotFoundError(extra={"group_id": group_id})
    
    firmware = get_object(Firmware, uuid=firmware_id)
    
    if firmware is None:
        raise NotFoundError(extra={"firmware_id": firmware_id})

    for device in group.devices.all():
        device = DeviceVersion.objects.update_or_create(
            device=device,
            defaults={"version": firmware.version}
        )
    
    group.firmware = firmware
    group.full_clean()
    group.save()
    
    return group