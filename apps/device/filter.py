import django_filters
from apps.device.models import Device

class DeviceFilter(django_filters.FilterSet):
    """
    Filtro para o modelo Device.
    Permite filtrar por ID e código.
    """
    class Meta:
        model = Device
        fields = ("uuid", "code")
