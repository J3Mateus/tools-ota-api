from django.http import Http404
from django.shortcuts import get_object_or_404

from apps.users.models import BaseUser


def user_get(*,pk: str) -> BaseUser | None:
    try:
        return get_object_or_404(BaseUser, id=pk)
    except Http404:
       return None