from apps.device.models import Device
from django.db import transaction

from utils import get_object

@transaction.atomic
def device_create(*, code: str) -> Device:
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
        code=code
    )
    instance_device.save()
    return instance_device
