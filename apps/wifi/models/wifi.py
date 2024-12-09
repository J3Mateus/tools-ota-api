from django.db import models
import uuid

from apps.common.models import BaseModel

class Wifi(BaseModel):
    uuid        = models.UUIDField(default=uuid.uuid4, unique=True)
    SSDI        = models.CharField('SSDI', max_length=50)
    password    = models.CharField('Senha', max_length=100)
  

    class Meta:
        app_label = 'wifi'
        db_table  = f'{app_label}'
