import pika

class Rabbit:
    def send_new_user(message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='new_user')

        channel.basic_publish(exchange='', routing_key='new_user', body=message)
        print("new_user:", message)
        connection.close()