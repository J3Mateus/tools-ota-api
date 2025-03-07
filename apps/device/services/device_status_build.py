from apps.core.exceptions import NotFoundError
from apps.device.models import DeviceStatusBuild, Device
from utils import get_object
from enum import Enum


class DeviceStatus(Enum):
    IN_BUILD = 'in_build'
    COMPLETED_BUILD = 'completed_build'
    IN_PROCESSING = 'in_processing'
    WAITING_TO_BE_RECEIVED = 'waiting_to_be_received'
    RECEIVED = 'received'

def device_status_build(*, device_code:str, status: DeviceStatus) -> DeviceStatusBuild:

    device = get_object(Device, code=device_code)

    if not device:
        raise NotFoundError(extra={
            "uuid": device_code
        })
    

    device_version,create = DeviceStatusBuild.objects.update_or_create(
        device=device,
        defaults={"status": status}
    )

    return device