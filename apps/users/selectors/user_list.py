from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404

from apps.users.filters import BaseUserFilter
from apps.users.models import BaseUser

def user_list(*, filters=None) -> QuerySet[BaseUser]:
    filters = filters or {}

    qs = BaseUser.objects.all()

    return BaseUserFilter(filters, qs).qs