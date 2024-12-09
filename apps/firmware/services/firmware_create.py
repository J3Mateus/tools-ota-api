from apps.firmware.models import Firmware
from django.db import transaction

@transaction.atomic
def firmware_create(*, name: str, version: str, code: str = None, link_bin: str = None) -> Firmware:
    """
    Cria um novo firmware.

    Args:
        name (str): Nome do firmware.
        version (str): Versão do firmware.
        code (str, optional): Código associado ao firmware.
        link_bin (str, optional): Link para o arquivo binário do firmware.

    Returns:
        Firmware: A instância criada do firmware.
    """
    instance_firmware = Firmware(
        name=name,
        version=version,
        code=code,
        link_bin=link_bin
    )
    instance_firmware.save()
    return instance_firmware
