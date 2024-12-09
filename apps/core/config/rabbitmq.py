from decouple import config
import pika


# Defina suas configurações do RabbitMQ usando o `decouple`
RABBITMQ_HOST = config('RABBITMQ_HOST', default='localhost')
RABBITMQ_PORT = config('RABBITMQ_PORT', default=5672, cast=int)  # Porta do RabbitMQ
RABBITMQ_QUEUE = config('RABBITMQ_QUEUE', default='default_queue')
RABBITMQ_USER = config('RABBITMQ_USER', default='guest')
RABBITMQ_PASSWORD = config('RABBITMQ_PASSWORD', default='guest')

# Função para estabelecer uma conexão com o RabbitMQ
def get_rabbitmq_connection():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,  # Usando a porta configurada
        credentials=credentials
    ))
    return connection
