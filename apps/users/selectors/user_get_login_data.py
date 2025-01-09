from apps.users.models import BaseUser
from django.shortcuts import get_object_or_404
from django.http import Http404

def user_get_login_data(*, user: BaseUser):
    try:
        return get_object_or_404(BaseUser, id=user.id)
    except Http404:
       return None