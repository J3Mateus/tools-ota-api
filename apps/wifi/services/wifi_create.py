from apps.wifi.models import Wifi
from django.db import transaction

@transaction.atomic
def wifi_create(*, SSDI: str, password: str):
    """
    Creates a Wifi instance.
    
    Args:
        SSDI (str): The name of the Wifi network.
        password (str): The password for the Wifi network.
    
    Returns:
        Wifi: The created Wifi instance.
    """
    instance_wifi = Wifi(
        SSDI=SSDI,
        password=password
    )
    
    instance_wifi.save()
    
    return instance_wifi
