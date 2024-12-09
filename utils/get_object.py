from typing import TypeVar, Union, Type, Optional
from django.db.models import Model, QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404
from apps.core.exceptions import NotFoundError

# Definir um TypeVar para representar o tipo de Model
T = TypeVar('T', bound=Model)

def get_object(model_or_queryset: Union[Type[T], QuerySet[T]], **kwargs) -> Optional[T]:
    """
    Reuse get_object_or_404 since the implementation supports both Model and queryset.
    Catch Http404 & return None if object is not found.
    """
    try:
        if hasattr(model_or_queryset, 'filter'):
            # Se for um queryset, verifique se 'is_deleted' existe antes de aplicar o filtro
            if 'is_deleted' in model_or_queryset.model._meta.get_fields():
                queryset = model_or_queryset.filter(is_deleted=False)
            else:
                queryset = model_or_queryset
            return get_object_or_404(queryset, **kwargs)
        else:
            # Se for um Model, verifique se 'is_deleted' existe antes de aplicar o filtro
            if 'is_deleted' in model_or_queryset._meta.get_fields():
                queryset = model_or_queryset.objects.filter(is_deleted=False)
            else:
                queryset = model_or_queryset.objects.all()
            return get_object_or_404(queryset, **kwargs)
    except Http404:
        return None
