from typing import Optional
from apps.device.models import Device
from apps.group.models import Group
from apps.core.exceptions import NotFoundError
from apps.users.models import BaseUser
from utils import get_object

def device_delete(*, id: str, user: BaseUser) -> Device:
    """
    Deleta um dispositivo pelo ID e remove ele de todos os grupos vinculados.

    Args:
        id (str): ID do dispositivo.
        user (BaseUser): Usuário responsável pela operação.

    Returns:
        Device: O dispositivo deletado.

    Raises:
        NotFoundError: Se o dispositivo não for encontrado.
    """
    # Busca o dispositivo
    device: Optional[Device] = get_object(Device, uuid=id)

    if device is None:
        raise NotFoundError(extra={"id": id})

    # Remove o dispositivo de todos os grupos vinculados
    groups = device.groups.all()
    for group in groups:
        group.devices.remove(device)

    # Deleta o dispositivo
    device.delete(user)

    return device
