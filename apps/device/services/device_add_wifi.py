from apps.core.exceptions import NotFoundError
from apps.wifi.models.wifi import Wifi
from apps.device.models import Device
from django.db import transaction

from utils import get_object

@transaction.atomic
def device_add_wifi(*,device_id:str,wifi_id: str) -> Device:
    """
    Adiciona um wifi a um device.

    Args:
        device_id (str): ID do device.
        wifi_id (str): ID do wifi.

    Returns:
        Device: A instância do device atualizada.
    """
    device = get_object(Device, uuid=device_id)

    if device is None:
        raise NotFoundError(extra={"device_id": device_id})
    
    wifi = get_object(Wifi, uuid=wifi_id)
    
    if wifi is None:
        raise NotFoundError(extra={"wifi_id": wifi_id})

    device.wifi = wifi
    device.full_clean()
    device.save()
    
    return device