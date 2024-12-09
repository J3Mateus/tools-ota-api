from django.db import models
from django.conf import settings

import uuid
from apps.common.models.base_model import BaseModel


class File(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True,)
    type = models.CharField(max_length=255,null=True, blank=True,) 
    file = models.FileField('Arquivo', null=True, blank=True, upload_to='files/') 
    
    @property
    def url(self):
        return f"http://localhost:8080{self.file.url}"
    
    class Meta:
        app_label = 'files'
        db_table  = f'{app_label}'