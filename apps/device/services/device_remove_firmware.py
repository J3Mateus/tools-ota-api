from apps.core.exceptions import NotFoundError
from apps.device.models import Device
from utils import get_object


def device_remove_firmware(*, device_uuid:str ) -> Device:
    
    device = get_object(Device, uuid=device_uuid)

    if not device:
        raise NotFoundError(extra={
            "uuid": device_uuid
        })
    

    device.firmware = None

    device.save()

    return device