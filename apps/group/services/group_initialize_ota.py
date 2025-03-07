from typing import Optional
from apps.core.services.rabbitmq_service import publish_message_to_queue
from apps.device.services import device_status_build
from apps.group.models import Group
from apps.core.exceptions import NotFoundError
from utils import get_object

def group_initialize_ota(*, uuid: str) -> Group:
    """
    Inicializa o OTA de um grupo.

    Args:
        uuid (str): UUID do grupo.

    Returns:
        Group: O grupo inicializado.

    Raises:
        NotFoundError: Se o grupo não for encontrado.
    """
    group: Optional[Group] = get_object(Group, uuid=uuid)

    if group is None:
        raise NotFoundError(extra={"uuid": uuid})
    
    if group.wifi is None:
        raise NotFoundError(message="Wifi não encontrado", extra={"uuid": uuid})
    
    if group.firmware is None:
        raise NotFoundError(message="Firmware não encontrado", extra={"uuid": uuid})

    if group.api_key is None:
        raise NotFoundError(message="Api Key não encontrado", extra={"uuid": uuid})
    
    devices = group.devices.all()
    for device in devices:
        device_status_build(device_code=device.code, status='in_processing')
        
    publish_message_to_queue(group.to_json())
    return group
