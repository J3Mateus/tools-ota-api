from apps.core.exceptions import NotFoundError
from apps.device.models.device import Device
from apps.device.models.device_version import DeviceVersion
from apps.firmware.models.firmware import Firmware
from utils import get_object
from django.db import transaction

@transaction.atomic
def device_update_version_current(*, device_id: str,firmware_id: str) -> DeviceVersion:
    """ Sinaliza qual é a versão que está rodando atualmente no device """

    device = get_object(Device, code=device_id)

    if not device:
        raise NotFoundError("Device not found")
    
    firmware = get_object(Firmware, uuid=firmware_id)

    if not firmware:
        raise NotFoundError("Firmware not found")

    device_version,create = DeviceVersion.objects.update_or_create(
        device=device,
        defaults={"version": firmware.version}
    )

    return device_version