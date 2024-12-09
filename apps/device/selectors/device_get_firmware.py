

from apps.core.exceptions import NotFoundError
from apps.device.models.device import Device
from apps.firmware.models.firmware import Firmware
from utils import get_object


def device_get_firmware(*,device_id: str) -> Firmware:
    """
    Retorna o firmware aplicado ao dispositivo com base na prioridade:
    1. Firmware diretamente associado ao dispositivo.
    2. Firmware do grupo ao qual o dispositivo pertence (se existir).
    """

    device = get_object(Device,code=device_id)

    if not device:
        raise NotFoundError("Device not found")
    
    firwmare = device.get_firmware()

    return firwmare