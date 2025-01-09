from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404

from apps.role.models import Roles
from apps.role.filters import RoleFilter

def role_get(role: Roles, id: str):
    try:
        return get_object_or_404(Roles, id=id)
    except Http404:
       return None


def role_list(*, filters=None) -> QuerySet[Roles]:
    filters = filters or {}

    qs = Roles.objects.all()

    return RoleFilter(filters, qs).qs
