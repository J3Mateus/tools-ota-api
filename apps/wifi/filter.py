import django_filters
from apps.wifi.models import Wifi

class WifiFilter(django_filters.FilterSet):
    """
    Filtro para o modelo Wifi.
    Permite filtrar por UUID, SSDI e password.
    """
    class Meta:
        model = Wifi
        fields = ("uuid", "SSDI", "password")
