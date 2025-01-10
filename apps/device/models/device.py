import json
import uuid
from django.db import models
from apps.common.models import BaseModel
from apps.firmware.models.firmware import Firmware
from apps.users.models import UserAPIKey
from apps.wifi.models.wifi import Wifi


class Device(BaseModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=255, unique=True)
    wifi = models.ForeignKey(
        Wifi,
        on_delete=models.CASCADE,
        related_name='devices',
        verbose_name='Wifi associado',
        null=True,  # Allow nulls temporarily
        blank=True  # Allow blank temporarily
    )
    firmware = models.ForeignKey(
        Firmware,
        on_delete=models.SET_NULL,
        null=True,  # Allow firmware to be null
        blank=True,
        related_name="devices",
        verbose_name="Firmware do dispositivo"
    )
    api_key = models.ForeignKey(
        UserAPIKey,
        on_delete=models.CASCADE,
        related_name="api_key_devices",
        verbose_name="Chave de API associada ao device",
        null=True,  # Allow nulls temporarily
        blank=True  # Allow blank temporarily
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
        group = self.groups.filter(is_deleted=False).first()  # Obtém o primeiro grupo ativo
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
    
    def to_json(self):
        """
        Converte uma instância do modelo Device para um formato JSON, incluindo informações dos modelos relacionados
        como Wifi e Firmware
        """

        def convert_uuid_to_str(obj):
            """Converte UUID para string recursivamente"""
            if isinstance(obj, uuid.UUID):
                return str(obj)
            elif isinstance(obj, dict):
                return {key: convert_uuid_to_str(value) for key, value in obj.items()}
            elif isinstance(obj, list):
                return [convert_uuid_to_str(item) for item in obj]
            return obj

        # Serializando campos relacionados (Wifi, Firmware, Devices)
        wifi_data = None
        if self.wifi:
            wifi_data = {
                'uuid': self.wifi.uuid,
                'SSDI': self.wifi.SSDI,
                'password': self.wifi.password,
            }

        firmware_data = None
        if self.firmware:
            firmware_data = {
                'uuid': self.firmware.uuid,
                'name': self.firmware.name,
                'version': self.firmware.version,
                'code': self.firmware.code,
            }
        
        api_key_data = None
        if self.api_key:
            api_key_data = {
                'uuid': self.api_key.id,
                'key': self.api_key.key
            }

        # Estruturando os dados do grupo
        device_data = {
            'uuid': self.uuid,
            'name': self.code,
            'active': self.is_deleted,
            'wifi': wifi_data,
            'firmware': firmware_data,
            'api_key': api_key_data,
            'devices': [],
        }

        # Convertendo UUIDs para string
        device_data = convert_uuid_to_str(device_data)

        # Retornando o JSON
        return json.dumps(device_data, ensure_ascii=False, indent=4)

    class Meta:
        app_label = 'device'
        db_table  = f'{app_label}'