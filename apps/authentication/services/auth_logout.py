import uuid

from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import BaseUser


def auth_logout(user: BaseUser,toker:str) -> BaseUser:
    user.jwt_key = uuid.uuid4()
    user.full_clean()
    user.save(update_fields=["jwt_key"])
    token = RefreshToken(toker)
    token.blacklist()
    return user