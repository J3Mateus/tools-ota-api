from django.db.models.query import QuerySet
from apps.wifi.filter import WifiFilter
from apps.wifi.models import Wifi

def wifi_list(*, filters=None) -> QuerySet[Wifi]:
    """
    Lista instâncias de Wifi com base nos filtros fornecidos.
    
    Args:
        filters (dict, optional): Um dicionário contendo os critérios de filtragem.
    
    Returns:
        QuerySet[Wifi]: Um QuerySet das instâncias filtradas de Wifi.
    """
    filters = filters or {}
    qs = Wifi.objects.all()

    return WifiFilter(filters, qs).qs
