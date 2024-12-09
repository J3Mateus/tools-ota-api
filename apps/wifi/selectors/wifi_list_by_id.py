from typing import Optional
from apps.wifi.models import Wifi
from apps.core.exceptions import NotFoundError
from utils import get_object

def wifi_list_by_id(*, uuid: str) -> Optional[Wifi]:
    """
    Busca uma instância de Wifi pelo UUID.
    
    Args:
        uuid (str): O UUID da instância de Wifi.
    
    Returns:
        Optional[Wifi]: A instância encontrada do modelo Wifi.
    
    Raises:
        NotFoundError: Se nenhuma instância com o UUID fornecido for encontrada.
    """
    wifi = get_object(Wifi, uuid=uuid)

    if wifi is None:
        raise NotFoundError(extra={
            "uuid": uuid
        })

    return wifi
