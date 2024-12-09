import logging

from django.db import models


LOG_LEVELS = [
    (logging.NOTSET, 'NotSet'),
    (logging.INFO, 'Info'),
    (logging.WARNING, 'Warning'),
    (logging.DEBUG, 'Debug'),
    (logging.ERROR, 'Error'),
    (logging.CRITICAL, 'Critial'),
]

class DbLog(models.Model):
    logger_name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(
        choices=LOG_LEVELS,
        default=logging.ERROR,
        db_index=True,
    )
    msg = models.TextField()
    trace = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'core'
        db_table = f'{app_label}_db_log'
        verbose_name = 'Logging'
        verbose_name_plural = 'Logging'
        ordering = ['-created']

    def __str__(self):
        return f'{self.msg}'
