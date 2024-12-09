from typing import Optional
from apps.device.models import Device
from apps.core.exceptions import NotFoundError
from utils import get_object

def device_list_by_id(*, id: str) -> Optional[Device]:
    """
    Busca um dispositivo pelo ID.

    Args:
        id (str): ID do dispositivo.

    Returns:
        Optional[Device]: A instância do dispositivo.

    Raises:
        NotFoundError: Se o dispositivo não for encontrado.
    """
    device = get_object(Device, uuid=id)

    if device is None:
        raise NotFoundError(extra={"id": id})

    return device
