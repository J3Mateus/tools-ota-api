from apps.core.exceptions import DuplicateResourceError
from apps.firmware.models import Firmware
from django.db import transaction

from apps.users.models import BaseUser
from utils import get_object

@transaction.atomic
def firmware_create(*, name: str, version: str, code: str = None,use_code: bool = True,user: BaseUser) -> Firmware:
    """
    Cria um novo firmware.

    Args:
        name (str): Nome do firmware.
        version (str): Versão do firmware.
        code (str, optional): Código associado ao firmware.
        use_code (bool, optional): Indica se o firmware vai precisar compilar o codigo.
        user (BaseUser): Usuário que está criando o firmware.

    Returns:
        Firmware: A instância criada do firmware.
    """

    # existent_firmware = get_object(Firmware,code=code)
    # if existent_firmware:
    #     raise DuplicateResourceError(extra={
    #         "code": code
    #     })
    
    instance_firmware = Firmware(
        name=name,
        version=version,
        code=code,
        use_code=use_code,
        created_by=user,
    )
    instance_firmware.save()
    return instance_firmware
