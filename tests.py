from docker_kafka_topics.producer import Producer
import requests
import json
import grpc
from docker_gRPC import schema_pb2_grpc
from docker_gRPC import schema_pb2

def test_rest(query):
    url = 'http://localhost:8000/predict'
    response = requests.get(url, params=query)

    if response.status_code == 200:
        result = response.json()
        print("Respuesta de REST: ", result)
    else:
        print("Error en la petición REST:", response.json())

def test_kafka(query):
    producer = Producer('request_predict_kafka', 'response_predict_kafka', 'group_1', 'client_response', ['localhost:29092'])
    producer.send_messages(query)

def test_gRPC(query):
    channel = grpc.insecure_channel('localhost:50051')
    stub = schema_pb2_grpc.TelefoniaServiceStub(channel)

    client_data = schema_pb2.ClientData(
        internet_service=query['internet_service'],
        number_dependents=query['number_dependents'],
        number_referrals=query['number_referrals'],
        satisfaction_score=query['satisfaction_score'],
        tenure_in_months=query['tenure_in_months'],
        total_long_distance_charges=query['total_long_distance_charges'],
        total_revenue=query['total_revenue'],
        contract=query['contract'],
        payment_method=query['payment_method']
    )

    response = stub.prediction(client_data)
    print("Respuesta de gRPC: ", response.pred)
    channel.close()

if __name__ == '__main__':
    # Datos de inferencia
    query = {
        'internet_service': 1,
        'number_dependents': 0,
        'number_referrals': 1,
        'satisfaction_score': 3,
        'tenure_in_months': 25,
        'total_long_distance_charges': 486.00,
        'total_revenue': 2677.15,
        'contract': 'Two Year',
        'payment_method': 'Mailed Check'
    }

    # Ejecutar prueba REST
    test_rest(query)

    # Ejecutar prueba Kafka
    test_kafka(query)

    # Ejecutar prueba gRPC
    test_gRPC(query)