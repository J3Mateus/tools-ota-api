from apps.core.exceptions import BadRequestError, DuplicateResourceError, NotFoundError
from apps.device.models import Device
from apps.users.models import UserAPIKey
from utils import get_object


def device_link_api_key(*, device_uuid:str,api_key_uuid: str) -> Device:

    """
    Link an api key to a device
    :param device_uuid:
    :param api_key_uuid:
    :return: Device
    """
    
    device = get_object(Device, uuid=device_uuid)

    if not device:
        raise NotFoundError(extra={
            "uuid": device_uuid
        })
    
    api_key = get_object(UserAPIKey, id=api_key_uuid)

    if not api_key:
        raise NotFoundError(extra={
            "uuid": api_key_uuid
        })
    
    if api_key.is_deleted:
        raise BadRequestError(extra={
            "api_key": "Api key is deleted"
        })
    
    device.api_key = api_key

    device.save()

    return device