import uuid
from django.db import models
from django.utils.crypto import get_random_string
from apps.common.models import BaseModel
from apps.firmware.models import Firmware


class Webhook(BaseModel):

    STATUS_CHOICES = [
        ('FINISH', 'Finish'),
        ('BUILD', 'Build'),
    ]

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    firmware = models.ForeignKey(Firmware, on_delete=models.CASCADE)
    url = models.URLField('URL', blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='BUILD'
    )

    def save(self, *args, **kwargs):
        if not self.url:
            random_path = get_random_string(16)
            self.url = f'https://example.com/webhook/{random_path}'
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'webhook'
        db_table  = f'{app_label}'
