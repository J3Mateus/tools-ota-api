import django_filters

from apps.role.models import Roles


class RoleFilter(django_filters.FilterSet):
    class Meta:
        model = Roles
        fields = ("id", "name", "code")