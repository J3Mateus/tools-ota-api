import django_filters
from apps.group.models import Group

class GroupFilter(django_filters.FilterSet):
    """
    Filtro para o modelo Group.
    Permite filtrar por UUID, nome e ativo/inativo.
    """
    class Meta:
        model = Group
        fields = ("uuid", "name", "active","is_deleted")
