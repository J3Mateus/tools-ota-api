from apps.device.models import Device
from django.db import transaction

from apps.users.models import BaseUser
from utils import get_object

@transaction.atomic
def device_create(*, code: str,user :BaseUser) -> Device:
    """
    Cria um novo dispositivo.

    Args:
        code (str): Código único do dispositivo.

    Returns:
        Device: A instância criada do dispositivo.
    """

    device = get_object(Device, code=code)

    if device:
        return device

    instance_device = Device(
        code=code,
        created_by=user
    )
    
    instance_device.save()
    return instance_device
