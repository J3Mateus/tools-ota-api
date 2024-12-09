from typing import Optional
from apps.firmware.models import Firmware
from apps.core.exceptions import NotFoundError
from utils import get_object

def firmware_list_by_id(*, uuid: str) -> Optional[Firmware]:
    """
    Busca um firmware pelo UUID.

    Args:
        uuid (str): UUID do firmware.

    Returns:
        Optional[Firmware]: A instância do firmware.

    Raises:
        NotFoundError: Se o firmware não for encontrado.
    """
    firmware = get_object(Firmware, uuid=uuid)

    if firmware is None:
        raise NotFoundError(extra={"uuid": uuid})

    return firmware
