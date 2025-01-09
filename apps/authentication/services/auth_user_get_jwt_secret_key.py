from apps.users.models import BaseUser

def auth_user_get_jwt_secret_key(user: BaseUser) -> str:
    return str(user.jwt_key)
