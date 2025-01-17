from apps.core.exceptions import BadRequestError, DuplicateResourceError, NotFoundError
from apps.group.models import Group
from apps.users.models import UserAPIKey
from utils import get_object


def group_link_api_key(*, group_uuid:str,api_key_uuid: str) -> Group:

    """
    Link an api key to a group
    :param group_uuid:
    :param api_key_uuid:
    :return: Group
    """
    
    group = get_object(Group, uuid=group_uuid)

    if not group:
        raise NotFoundError(extra={
            "uuid": group_uuid
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
    
    group.api_key = api_key
    print(api_key)
    group.save()

    return group