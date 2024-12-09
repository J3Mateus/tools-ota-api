from django.db import models
import uuid

from apps.common.models import BaseModel
from apps.device.models import Device
from apps.group.models import Group

class GroupDevice(BaseModel):
    uuid        = models.UUIDField(default=uuid.uuid4, unique=True)
    group       = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_device')
    device      = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='group_device')

    class Meta:
        app_label = 'group'
        db_table  = f'{app_label}_firmware'
