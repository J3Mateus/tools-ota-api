from typing import Dict, Tuple
from django.db import transaction
from apps.common.services.model_update import model_update
from apps.firmware.models import Firmware

@transaction.atomic
def firmware_update(*, firmware: Firmware, data: Dict[str, any]) -> Tuple[Firmware, bool]:
    """
    Atualiza os dados de um firmware.

    Args:
        firmware (Firmware): Instância do firmware a ser atualizada.
        data (Dict[str, any]): Dados para atualização.

    Returns:
        Tuple[Firmware, bool]: A instância atualizada e um booleano indicando se houve mudanças.
    """
    fields = ['name', 'version', 'code', 'use_code']

    new_firmware, has_updated, logs = model_update(instance=firmware, fields=fields, data=data)

    return new_firmware, has_updated
