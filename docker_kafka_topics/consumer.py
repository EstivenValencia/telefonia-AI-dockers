import sys
import os
from telefonica import TelefonicaAI
import json
from http import client
import threading
from kafka import KafkaConsumer, KafkaProducer
import queue

class Consumer:
    def __init__(self, topic_request, topic_response, group_id, client_id, host:list, model_path: str, scaler_path:str, significant_columns_path: str):
        self.telefonicaAI = TelefonicaAI(model_path, scaler_path, significant_columns_path)

        self.queue_request = queue.Queue() 

        self.topic_request = topic_request
        self.topic_respose = topic_response

        self.hosts = host

        self.group_id = group_id
        self.client_id = client_id

        self.producer_response = KafkaProducer(
                                      bootstrap_servers=self.hosts,
                                      key_serializer=lambda x: json.dumps(x).encode('utf-8'),
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        
        self.consumer_request = KafkaConsumer(
                                        self.topic_request, 
                                        client_id=self.client_id, 
                                        group_id=self.group_id,
                                        bootstrap_servers=self.hosts,
                                        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                                        key_deserializer=lambda v: json.loads(v.decode('utf-8')),
                                        max_poll_records=10
        )

        self.thread_request = threading.Thread(target=self.consume_request)

        self.thread_request.start()
    def consume_request(self):

        for message in self.consumer_request:
            self.queue_request.put(message)
            print(f'Peticion recibida id: {message.key['id']}')



    def inference(self):
        while True:
            message = self.queue_request.get()

            key = message.key
            response = self.telefonicaAI.predict(message.value)

            self.producer_response.send(self.topic_respose, key=key, value={'prediction': response})


if __name__ == '__main__':
    print("Iniciando el consumidor Kafka")
    
    model_path = 'models/best_random_forest_model.joblib'
    scaler_path ='models/scaler.pkl'
    significant_columns_path ='models/significant_columns.pkl'

    consumer = Consumer('request_predict_kafka', 'response_predict_kafka', 'group_1', 'client_request', ['kafka:9092'],
                        model_path, scaler_path, significant_columns_path)
    consumer.inference()