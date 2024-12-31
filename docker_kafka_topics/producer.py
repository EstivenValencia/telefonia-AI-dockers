from kafka import KafkaProducer
from kafka import KafkaConsumer

import threading

import time
import json
from time import sleep
import uuid

class Producer:
    def __init__(self, topic_request, topic_response, group_id, client_id, host:list):
        self.topic_request = topic_request
        self.topic_respose = topic_response

        self.hosts = host

        self.group_id = group_id
        self.client_id = client_id

        self.producer_request = KafkaProducer(
                                      bootstrap_servers=self.hosts,
                                      key_serializer=lambda x: json.dumps(x).encode('utf-8'),
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        
        self.consumer_response = KafkaConsumer(
                                        self.topic_respose, 
                                        client_id=self.client_id, 
                                        group_id=self.group_id,
                                        bootstrap_servers=self.hosts,
                                        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                                        key_deserializer=lambda v: json.loads(v.decode('utf-8')),
                                        max_poll_records=10
        )

        thread_response = threading.Thread(target=self.receive_response)

        # Iniciar los hilos
        thread_response.start()

    def send_messages(self, value):

        self.key = {'id': str(uuid.uuid4())}
        self.producer_request.send(self.topic_request, key=self.key, value=value)
        print(f'Mensaje enviado a kafka con id: {self.key['id']} ')

        self.producer_request.flush()

    def receive_response(self):
        for message in self.consumer_response:
            print(f'Respuesta de inferencia desde kafka: {message.value['prediction']} - id: {message.key['id']}')

            break

if __name__ == '__main__':
    producer = Producer('request_predict_kafka', 'response_predict_kafka', 'group_1', 'client_response', ['localhost:29092'])

    data = [
        {
            'Internet Service':1,
            'Number of Dependents':0,
            'Number of Referrals':1,
            'Satisfaction Score':3,
            'Tenure in Months':25,
            'Total Long Distance Charges':486.00,
            'Total Revenue':2677.15,
            'Contract':'Two Year',
            'Payment Method':'Mailed Check'
        },
        {
            'Internet Service':0,
            'Number of Dependents':0,
            'Number of Referrals':1,
            'Satisfaction Score':3,
            'Tenure in Months':25,
            'Total Long Distance Charges':486.00,
            'Total Revenue':2677.15,
            'Contract':'Two Year',
            'Payment Method':'Mailed Check'

        }
    ]

    producer.send_messages(data)