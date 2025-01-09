from django.http import Http404
from django.shortcuts import get_object_or_404

from apps.users.models import BaseUser

def get_user_by_email(*,email:str) -> BaseUser:
    try:
        return get_object_or_404(BaseUser, email=email)
    except Http404:
       return None
   