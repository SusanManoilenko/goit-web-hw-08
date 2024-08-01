# producer.py
import pika
from models import Contact
from faker import Faker

fake = Faker()

def create_contacts(n):
    contacts = []
    for _ in range(n):
        contact = Contact(
            full_name=fake.name(),
            email=fake.email(),
            additional_info=fake.text()
        )
        contact.save()
        contacts.append(contact)
    return contacts

def send_to_queue(contacts):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue')

    for contact in contacts:
        channel.basic_publish(exchange='',
                              routing_key='email_queue',
                              body=str(contact.id))
        print(f"[x] Sent {contact}")

    connection.close()

if __name__ == "__main__":
    num_contacts = 10  # Кількість контактів для генерації
    contacts = create_contacts(num_contacts)
    send_to_queue(contacts)
