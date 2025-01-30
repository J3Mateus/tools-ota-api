from typing import Optional
from apps.device.models import Device
from apps.core.exceptions import NotFoundError
from utils import get_object

def device_undelete(*, id: str) -> Device:
    """
    Ativa novamente um dispositivo pelo ID

    Args:
        id (str): ID do dispositivo.

    Returns:
        Device: O dispositivo.

    Raises:
        NotFoundError: Se o dispositivo não for encontrado.
    """
    # Busca o dispositivo
    device: Optional[Device] = get_object(Device, uuid=id)

    if device is None:
        raise NotFoundError(extra={"id": id})

    # Deleta o dispositivo
    device.undelete()

    return device
