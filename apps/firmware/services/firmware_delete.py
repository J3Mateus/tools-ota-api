from typing import Optional
from apps.firmware.models import Firmware
from apps.core.exceptions import NotFoundError
from utils import get_object

def firmware_delete(*, uuid: str) -> Firmware:
    """
    Deleta um firmware pelo UUID.

    Args:
        uuid (str): UUID do firmware.

    Returns:
        Firmware: O firmware deletado.

    Raises:
        NotFoundError: Se o firmware não for encontrado.
    """
    firmware: Optional[Firmware] = get_object(Firmware, uuid=uuid)

    if firmware is None:
        raise NotFoundError(extra={"uuid": uuid})

    firmware.delete()
    return firmware
