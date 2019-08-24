import pika

class Rabbit:
    @staticmethod
    def send_new_user(message):
        credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
        parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue='new_user')

        channel.basic_publish(exchange='', routing_key='new_user', body=message)
        print("new_user:", message)
        connection.close()