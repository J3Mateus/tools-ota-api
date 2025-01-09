from django.db.models.query import QuerySet
from apps.core.exceptions import NotFoundError
from apps.users.models import BaseUser, UserAPIKey
from utils import get_object

def user_get_list_api_key(*,user_id: str) -> QuerySet[UserAPIKey]:

    user = get_object(BaseUser, id=user_id)

    if not user:
        raise NotFoundError(extra={
            "uuid": user_id
        })

    user_api_keys = UserAPIKey.objects.filter(user=user,is_deleted=False)
    

    return user_api_keys