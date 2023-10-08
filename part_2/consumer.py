import pika
import time
import json
from models import Contacts
import connect

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f" [x] Received {message}")
    contact = Contacts.objects(id = message['id'])[0]
    message_to_email = message['text_message']
    send_email_to(contact.email, message_to_email)
    contact.send_message = True
    contact.save()
    time.sleep(0.5)
    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def send_email_to(email, message):
    print(f"Message: '{message}' to email: '{email}' was sent")
 

   
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()