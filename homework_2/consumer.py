# consumer.py
import pika
from models import Contact


def send_email_stub(contact):
    # Заглушка функції відправки email
    print(f"Sending email to {contact.email}...")
    # Імітація відправки email
    return True


def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()

    if contact:
        if send_email_stub(contact):
            contact.email_sent = True
            contact.save()
            print(f"[x] Email sent and status updated for {contact}")


def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue')

    channel.basic_consume(queue='email_queue',
                          on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    consume()
