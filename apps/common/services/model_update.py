from typing import Any, Dict, List, Tuple
from django.db import models
from django.utils import timezone
from apps.common.types.django_model_type import DjangoModelType

def model_update(
    *, instance: DjangoModelType, fields: List[str], data: Dict[str, Any], auto_updated_at=True
) -> Tuple[DjangoModelType, bool, str]:
    if instance is None:
        return None, False, "Instância não fornecida."

    has_updated = False
    m2m_data = {}
    update_fields = []
    model_fields = {field.name: field for field in instance._meta.get_fields()}
    error_message = ""

    for field in fields:
        if field not in data:
            continue

        model_field = model_fields.get(field)

        if isinstance(model_field, models.ManyToManyField):
            m2m_data[field] = data[field]
            continue

        if isinstance(model_field, models.ForeignKey):
            # Handle ForeignKey fields
            related_model = model_field.remote_field.model
            foreign_key_id = data[field]
            try:
                related_instance = related_model.objects.get(id=foreign_key_id)
            except related_model.DoesNotExist:
                error_message += f"Erro: O valor de '{field}' não corresponde a um registro válido na tabela {related_model._meta.model_name}.\n"
                continue  # Não atualiza este campo se o ID for inválido

            if getattr(instance, field) != related_instance:
                has_updated = True
                update_fields.append(field)
                setattr(instance, field, related_instance)

        elif getattr(instance, field) != data[field]:
            has_updated = True
            update_fields.append(field)
            setattr(instance, field, data[field])

    if has_updated:
        if auto_updated_at:
            if "updated_at" in model_fields and "updated_at" not in update_fields:
                update_fields.append("updated_at")
                instance.updated_at = timezone.now()

        try:
            instance.full_clean()  # Valida os dados do modelo
            instance.save(update_fields=update_fields)
        except Exception as e:
            error_message += f"Erro ao salvar a instância: {str(e)}\n"
            return instance, False, error_message

    for field_name, value in m2m_data.items():
        try:
            related_manager = getattr(instance, field_name)
            related_manager.set(value)
            has_updated = True
        except Exception as e:
            error_message += f"Erro ao atualizar campo ManyToMany '{field_name}': {str(e)}\n"

    if error_message:
        return instance, False, error_message

    return instance, has_updated, "Atualização bem-sucedida."
