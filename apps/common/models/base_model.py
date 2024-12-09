from django.db import models
from tools_ota import settings
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now,verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True,null=True, verbose_name='Data de Atualização')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Deletion Date/Time')

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Created By',
        related_name='%(class)s_created_by',
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Updated By',
        related_name='%(class)s_updated_by',
    )

    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Deleted By',
        related_name='%(class)s_deleted_by',
    )

    is_deleted = models.BooleanField(default=False, verbose_name='Excluído', db_index=True)

    class Meta:
        abstract = True

    def delete(self, deleted_by = None):
        self.is_deleted = True
        self.deleted_by = deleted_by
        self.deleted_at = timezone.now()
        self.save()

    def undelete(self):
        self.is_deleted = False
        self.save()
