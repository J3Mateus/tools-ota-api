from django.db.models.query import QuerySet
from apps.firmware.filter import FirmwareFilter
from apps.firmware.models import Firmware
from apps.users.models import BaseUser

def firmware_list(*, filters=None,user: BaseUser) -> QuerySet[Firmware]:
    """
    Lista instâncias de Firmware com base nos filtros fornecidos.

    Args:
        filters (dict, optional): Filtros para aplicação.

    Returns:
        QuerySet[Firmware]: Instâncias filtradas do modelo Firmware.
    """
    filters = filters or {}
    qs = Firmware.objects.filter(created_by=user)

    return FirmwareFilter(filters, qs).qs
