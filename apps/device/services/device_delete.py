from typing import Optional
from apps.device.models import Device
from apps.core.exceptions import NotFoundError
from utils import get_object

def device_delete(*, id: str) -> Device:
    """
    Deleta um dispositivo pelo ID.

    Args:
        id (str): ID do dispositivo.

    Returns:
        Device: O dispositivo deletado.

    Raises:
        NotFoundError: Se o dispositivo não for encontrado.
    """
    device: Optional[Device] = get_object(Device, uuid=id)

    if device is None:
        raise NotFoundError(extra={"id": id})

    device.delete()
    return device
