from typing import Optional
from apps.core.services.rabbitmq_service import publish_message_to_queue
from apps.device.models import Device
from apps.core.exceptions import NotFoundError
from utils import get_object

def device_initialize_ota(*, uuid: str) -> Device:
    """
    Inicializa o OTA de um device.

    Args:
        uuid (str): UUID do device.

    Returns:
        Device: O device inicializado.

    Raises:
        NotFoundError: Se o grupo não for encontrado.
    """
    device: Optional[Device] = get_object(Device, uuid=uuid)

    if device is None:
        raise NotFoundError(extra={"uuid": uuid})
    
    if device.wifi is None:
        raise NotFoundError(message="Wifi não encontrado", extra={"uuid": uuid})
    
    if device.firmware is None:
        raise NotFoundError(message="Firmware não encontrado", extra={"uuid": uuid})

    publish_message_to_queue(device.to_json())
    return device
