import uuid
from django.db import models
from apps.common.models import BaseModel
from apps.device.models.device import Device


class DeviceVersion(BaseModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.CharField(max_length=255)
    device = models.ForeignKey(
        Device,
        on_delete=models.SET_NULL,
        null=True,  # Allow firmware to be null
        blank=True,
        related_name="devices",
        verbose_name="Devices com seus codigos"
    )

    def __str__(self) -> str:
        return self.version

    class Meta:
        app_label = 'device'
        db_table  = f'{app_label}_version'