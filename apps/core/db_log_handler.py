import logging

from django.conf import settings


db_default_formatter = logging.Formatter()


class DbLogHandler(logging.Handler):
    def emit(self, record):
        from apps.core.models import DbLog

        trace = None

        if record.exc_info:
            trace = db_default_formatter.formatException(record.exc_info)

        if settings.DJANGO_DB_LOGGER_ENABLE_FORMATTER:
            msg = self.format(record)
        else:
            msg = record.getMessage()

        kwargs = {
            'logger_name': record.name,
            'level': record.levelno,
            'msg': msg,
            'trace': trace
        }

        DbLog.objects.create(**kwargs)

    def format(self, record):
        if self.formatter:
            fmt = self.formatter
        else:
            fmt = db_default_formatter

        if type(fmt) == logging.Formatter:
            record.message = record.getMessage()

            if fmt.usesTime():
                record.asctime = fmt.formatTime(record, fmt.datefmt)

            # ignore exception traceback and stack info

            return fmt.formatMessage(record)
        else:
            return fmt.format(record)


class DbLogHandlerWithIPAddress(DbLogHandler):
    def emit(self, record):
        record.ip = '0.0.0.0'

        try:
            x_forwarded_for = record.request.META.get('HTTP_X_FORWARDED_FOR')

            if x_forwarded_for:
                record.ip = x_forwarded_for.split(',')[0]
            else:
                record.ip = record.request.META.get('REMOTE_ADDR')
        except:
            pass

        super().emit(record=record)
