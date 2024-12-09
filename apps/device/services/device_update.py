from typing import Dict, Tuple
from django.db import transaction
from apps.common.services.model_update import model_update
from apps.device.models import Device

@transaction.atomic
def device_update(*, device: Device, data: Dict[str, any]) -> Tuple[Device, bool]:
    """
    Atualiza os dados de um dispositivo.

    Args:
        device (Device): Instância do dispositivo a ser atualizada.
        data (Dict[str, any]): Dados para atualização.

    Returns:
        Tuple[Device, bool]: A instância atualizada e um booleano indicando se houve mudanças.
    """
    fields = ['code']

    new_device, has_updated, logs = model_update(instance=device, fields=fields, data=data)

    return new_device, has_updated
