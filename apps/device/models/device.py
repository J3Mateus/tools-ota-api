import uuid
from django.db import models
from apps.common.models import BaseModel
from apps.firmware.models.firmware import Firmware


class Device(BaseModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=255, unique=True)
    firmware = models.ForeignKey(
        Firmware,
        on_delete=models.SET_NULL,
        null=True,  # Allow firmware to be null
        blank=True,
        related_name="devices",
        verbose_name="Firmware do dispositivo"
    )

    def get_firmware(self):
        """
        Retorna o firmware aplicado ao dispositivo com base na prioridade:
        1. Firmware diretamente associado ao dispositivo.
        2. Firmware do grupo ao qual o dispositivo pertence (se existir).
        """
        if self.firmware:  # Prioridade ao firmware do dispositivo
            return self.firmware

        # Verificar se o dispositivo está associado a um grupo ativo
        group = self.groups.filter(active=True).first()  # Obtém o primeiro grupo ativo
        if group and group.firmware:
            return group.firmware

        return None  # Nenhum firmware associado
    
    def unlink_firmware(self):
        """
        Remove o vínculo do firmware do dispositivo.
        """
        self.firmware = None
        self.save()

    def __str__(self):
        return self.code

    class Meta:
        app_label = 'device'
        db_table  = f'{app_label}'