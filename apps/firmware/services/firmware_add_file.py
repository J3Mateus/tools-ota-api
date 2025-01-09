from typing import List
from django.db import transaction
from django.core.files.uploadedfile import UploadedFile
from apps.core.exceptions import NotFoundError
from apps.files.models import File
from apps.firmware.models import Firmware
from utils import get_object


@transaction.atomic
def firmware_add_file(*,
                       firmware_id: str,
                       file: UploadedFile,
                       ) -> Firmware:
    
    firmware = get_object(Firmware,uuid=firmware_id)
    
    if not firmware :
        raise NotFoundError(extra={
            "firmware_id": firmware_id
        })
        

    instance_file = File(
        name=file.name,
        type=file.content_type,
        file=file,
    )

    instance_file.save()

    firmware.file =  instance_file
   
    firmware.save()

    return firmware