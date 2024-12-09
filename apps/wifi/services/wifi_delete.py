from typing import Optional
from apps.wifi.models import Wifi
from apps.core.exceptions import NotFoundError
from utils import get_object

def wifi_delete(*, uuid: str) -> Wifi:
    """
    Deletes a Wifi instance by its UUID.
    
    Args:
        uuid (str): The UUID of the Wifi instance to delete.
    
    Returns:
        Wifi: The deleted Wifi instance.
    
    Raises:
        NotFoundError: If no Wifi instance with the given UUID is found.
    """
    wifi: Optional[Wifi] = get_object(Wifi, uuid=uuid)

    if wifi is None:
        raise NotFoundError(extra={
            "uuid": uuid
        })
    
    wifi.delete()
    return wifi
