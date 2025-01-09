from django.db.models.query import QuerySet
from apps.device.filter import DeviceFilter
from apps.device.models import Device
from apps.users.models import BaseUser

def device_list(*, filters=None,user: BaseUser) -> QuerySet[Device]:
    """
    Lista instâncias de Device com base nos filtros fornecidos.

    Args:
        filters (dict, optional): Filtros para aplicação.

    Returns:
        QuerySet[Device]: Instâncias filtradas do modelo Device.
    """
    filters = filters or {}
    qs = Device.objects.filter(created_by=user)

    return DeviceFilter(filters, qs).qs
