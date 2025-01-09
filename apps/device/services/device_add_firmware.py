from apps.core.exceptions import NotFoundError
from apps.firmware.models.firmware import Firmware
from apps.device.models import Device
from django.db import transaction

from utils import get_object

@transaction.atomic
def device_add_firmware(*,device_id: str, firmware_id: str) -> Device:
    """
    Adiciona um firmware a um device.

    Args:
        device_id (str): ID do device.
        firmware_id (str): ID do firmware.

    Returns:
        Device: A instância do device atualizada.
    """
    device = get_object(Device, uuid=device_id)

    if device is None:
        raise NotFoundError(extra={"device_id": device_id})
    
    firmware = get_object(Firmware, uuid=firmware_id)
    
    if firmware is None:
        raise NotFoundError(extra={"firmware_id": firmware_id})

    device.firmware = firmware
    device.full_clean()
    device.save()
    
    return device