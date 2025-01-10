import json
from django.db import models
import uuid
from apps.common.models import BaseModel
from apps.firmware.models import Firmware
from apps.device.models import Device
from apps.users.models import UserAPIKey
from apps.wifi.models import Wifi

class Group(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField('Nome do grupo', max_length=100)
    active = models.BooleanField('Ativo', default=True)
    wifi = models.ForeignKey(
        Wifi,
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Wifi associado',
        null=True,  # Allow nulls temporarily
        blank=True  # Allow blank temporarily
    )
    firmware = models.ForeignKey(
        Firmware,
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Firmware associado',
        null=True,  # Allow nulls temporarily
        blank=True  # Allow blank temporarily
    )
    devices = models.ManyToManyField(
        Device,
        through='GroupDevice',
        related_name='groups',
        verbose_name='Dispositivos do Grupo',
        through_fields=('group', 'device'),
        null=True,  # Allow nulls temporarily
        blank=True  # Allow blank temporarily
    )
    user = models.ForeignKey(
        'users.BaseUser',
        on_delete=models.CASCADE,
        related_name="users",
        verbose_name="Usuario associado ao grupo",
        null=True,  # Allow nulls temporarily
        blank=True  # Allow blank temporarily
    )
    api_key = models.ForeignKey(
        UserAPIKey,
        on_delete=models.CASCADE,
        related_name="api_keys",
        verbose_name="Chave de API associada ao grupo",
        null=True,  # Allow nulls temporarily
        blank=True  # Allow blank temporarily
    )

    def unlink_firmware(self):
        """
        Remove o vínculo do firmware do grupo.
        """
        self.firmware = None
        self.save()    
        
    def to_json(self):
        """
        Converte uma instância do modelo Group para um formato JSON, incluindo informações dos modelos relacionados
        como Wifi, Firmware e Dispositivos.
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

        devices_data = []
        if self.devices.exists():
            devices_data = list(self.devices.values('uuid', 'code'))  # Incluindo os campos relevantes de cada dispositivo

        api_key_data = None
        if self.api_key:
            api_key_data = {
                'uuid': self.api_key.id,
                'key': self.api_key.key
            }

        # Estruturando os dados do grupo
        group_data = {
            'uuid': self.uuid,
            'name': self.name,
            'active': self.active,
            'wifi': wifi_data,
            'firmware': firmware_data,
            'devices': devices_data,
            'api_key': api_key_data,            
        }

        # Convertendo UUIDs para string
        group_data = convert_uuid_to_str(group_data)

        # Retornando o JSON
        return json.dumps(group_data, ensure_ascii=False, indent=4)
    
    def __str__(self):
        return self.name

    class Meta:
        app_label = 'group'
        db_table = f'{app_label}'
