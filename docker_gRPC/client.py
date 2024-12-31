import json
import grpc
import schema_pb2_grpc, schema_pb2
def test_gRPC(query):
    channel = grpc.insecure_channel('localhost:50051')
    stub = schema_pb2_grpc.TelefoniaServiceStub(channel)

    response = stub.prediction(schema_pb2.ClientData(json.dumps(query)))
    print("Respuesta de gRPC: ", response)
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

    # Ejecutar prueba gRPC
    test_gRPC(query)