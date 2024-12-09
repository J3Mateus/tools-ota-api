import uuid
from django.db import models
from apps.common.models import BaseModel
from apps.files.models import File

class Firmware(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    code = models.TextField(blank=True, null=True)
    link_bin = models.URLField(blank=True, null=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='firmware', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.version}"

    class Meta:
        app_label = 'firmware'
        db_table  = f'{app_label}'
