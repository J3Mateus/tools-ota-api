import django_filters
from apps.firmware.models import Firmware

class FirmwareFilter(django_filters.FilterSet):
    """
    Filtro para o modelo Firmware.
    Permite filtrar por UUID, nome e versão.
    """
    class Meta:
        model = Firmware
        fields = ("uuid", "name", "version","is_deleted")
