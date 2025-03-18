import uuid
from django.db import models
from apps.common.models import BaseModel
from apps.device.models.device import Device


class DeviceStatusBuild(BaseModel):
    IN_PROCESSING = 'in_processing'
    IN_BUILD = 'in_build'
    COMPLETED_BUILD = 'completed_build'
    WAITING_TO_BE_RECEIVED = 'waiting_to_be_received'
    RECEIVED = 'received'

    STATUS_CHOICES = [
        (IN_BUILD, 'In Build'),
        (COMPLETED_BUILD, 'Completed Build'),
        (IN_PROCESSING, 'In Processing'),
        (WAITING_TO_BE_RECEIVED, 'Waiting to be Received'),
        (RECEIVED, 'Received')
    ]

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey(
        Device,
        on_delete=models.SET_NULL,
        null=True,  # Allow firmware to be null
        blank=True,
        related_name="devices_status",
        verbose_name="Devices com status"
    )
    status = models.CharField(
        max_length=22,
        choices=STATUS_CHOICES,
        default=IN_PROCESSING,
        verbose_name="Status"
    )

    def __str__(self) -> str:
        return self.version

    class Meta:
        app_label = 'device'
        db_table  = f'{app_label}_status_build'