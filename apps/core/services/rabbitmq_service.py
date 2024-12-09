import json
import pika
from apps.core.config.rabbitmq import get_rabbitmq_connection, RABBITMQ_QUEUE

def publish_message_to_queue(message):
    # Conectar-se ao RabbitMQ
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    # Declare a fila (isso garante que a fila exista antes de enviar a mensagem)
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

    # Enviar a mensagem (convertendo para JSON)
    channel.basic_publish(
        exchange='',
        routing_key=RABBITMQ_QUEUE,
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2,  # Torna a mensagem persistente
        )
    )

    print(f"Mensagem enviada para a fila {RABBITMQ_QUEUE}: {message}")
    
    # Fechar a conexão
    connection.close()
