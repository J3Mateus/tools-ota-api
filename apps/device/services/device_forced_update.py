from apps.core.exceptions import NotFoundError
from apps.device.models.device import Device
from apps.device.models.device_version import DeviceVersion
from apps.firmware.models.firmware import Firmware
from utils import get_object
from django.db import transaction

@transaction.atomic
def device_forced_update(*, device_id: str) -> DeviceVersion:
    """ Sinaliza qual é a versão que está rodando atualmente no device """

    device = get_object(Device, uuid=device_id)

    if not device:
        raise NotFoundError("Device not found")
    
    device_version,create = DeviceVersion.objects.update_or_create(
        device=device,
        defaults={"version": "0.0.0"}
    )

    return device_version