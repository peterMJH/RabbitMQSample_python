import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='MJH', durable=True)

msg = ' '.join(sys.argv[1:]) or "RabbitMQ Sample"

channel.basic_publish(
    exchange='',
    routing_key='MJH',
    body=msg,
    properties=pika.BasicProperties(delivery_mode=2)
)

print(" == Sent %r" %msg)
connection.close()