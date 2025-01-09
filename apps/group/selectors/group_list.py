from django.db.models.query import QuerySet
from apps.group.filter import GroupFilter
from apps.group.models import Group
from apps.users.models import BaseUser

def group_list(*, filters=None, user : BaseUser) -> QuerySet[Group]:
    """
    Lista instâncias de Group com base nos filtros fornecidos.

    Args:
        filters (dict, optional): Filtros para aplicação.

    Returns:
        QuerySet[Group]: Instâncias filtradas do modelo Group.
    """
    filters = filters or {}
    qs = Group.objects.filter(created_by=user)

    return GroupFilter(filters, qs).qs
