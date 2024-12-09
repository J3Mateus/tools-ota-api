

from apps.core.exceptions import NotFoundError
from apps.device.models.device_version import DeviceVersion
from utils import get_object


def device_get_current_version(*, device_id: str) -> DeviceVersion:
    """
    Retorna a versão atual do dispositivo.

    Args:
        device_id (str): ID do dispositivo.

    Returns:
        DeviceVersion: A versão atual do dispositivo.
    """
    device_version = get_object(DeviceVersion, device__code=device_id)

    if not device_version:
        raise NotFoundError("Device not found")

    return device_version