from apps.users.models import BaseUser
from rest_framework_simplejwt.tokens import AccessToken

def get_user_from_access_token_in_django_rest_framework_simplejwt(token: str) -> BaseUser:
  access_token_obj = AccessToken(token)
  user = BaseUser.objects.get(id=access_token_obj['user_id'])
  return user