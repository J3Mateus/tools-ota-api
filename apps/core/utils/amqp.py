import pika

from decouple import config


def get_credentials():
    _user = config('DJANGO_CHECKIN_AMQP_USER', default='guest')
    _pass = config('DJANGO_CHECKIN_AMQP_PASS', default='guest')

    return pika.PlainCredentials(_user, _pass)


def get_parameters():
    credentials = get_credentials()

    _host = config('DJANGO_CHECKIN_AMQP_HOST', default='localhost')
    _port = config('DJANGO_CHECKIN_AMQP_PORT', default=5672, cast=int)
    _virtual_host = config('DJANGO_CHECKIN_AMQP_VIRTUAL_HOST', default='/')
    _connection_name = config('DJANGO_CHECKIN_AMQP_CONNECTION_NAME', default='checkin')


    return pika.ConnectionParameters(
        host=_host,
        port=_port,
        virtual_host=_virtual_host,
        credentials=credentials,
        client_properties={
            'connection_name': _connection_name,
        },
    )


def get_connection():
    parameters = get_parameters()

    return pika.BlockingConnection(parameters)