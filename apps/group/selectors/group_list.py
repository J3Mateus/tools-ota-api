from django.db.models.query import QuerySet
from apps.group.filter import GroupFilter
from apps.group.models import Group

def group_list(*, filters=None) -> QuerySet[Group]:
    """
    Lista instâncias de Group com base nos filtros fornecidos.

    Args:
        filters (dict, optional): Filtros para aplicação.

    Returns:
        QuerySet[Group]: Instâncias filtradas do modelo Group.
    """
    filters = filters or {}
    qs = Group.objects.all()

    return GroupFilter(filters, qs).qs
