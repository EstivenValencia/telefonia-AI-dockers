# Unary gRPC, el método más simple en el que se llama y se calcula
# Existen otros tipos: Server Streaming, Client Streaming, Bidirectionar Streaming

import sys
import os

import grpc
from concurrent import futures
import json

# IMPORT DE STUBS COMPILADOS
import schema_pb2
import schema_pb2_grpc
from telefonica import TelefonicaAI
from google.protobuf.json_format import MessageToJson


# Modelo de prediccion
model_path = 'models/best_random_forest_model.joblib'
scaler_path ='models/scaler.pkl'
significant_columns_path ='models/significant_columns.pkl'
telefonicaAI = TelefonicaAI(model_path, scaler_path, significant_columns_path)


# Class to implememt the gRPC service
# This class must use as base class the generated in the stub
class ClassForServiceServicer(schema_pb2_grpc.TelefoniaServiceServicer):
    
    def prediction(self, request, context):
        data = {
            "internet_service": request.internet_service,
            "number_dependents": request.number_dependents,
            "number_referrals": request.number_referrals,
            "satisfaction_score": request.satisfaction_score,
            "tenure_in_months": request.tenure_in_months,
            "total_long_distance_charges": request.total_long_distance_charges,
            "total_revenue": request.total_revenue,
            "contract": request.contract,
            "payment_method": request.payment_method

        }

        pred = telefonicaAI.predict(data)

        # We generate the response
        # It depens on the gRPC response message
        return schema_pb2.PredictionResponse(
            pred=pred
        )

# CREATE SERVER: Function to launch the server
def create_server():

    # We create the server (please be careful with the max amount of workers/connections)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Now is the moment to add the service to the server
    # Please, take into account that this part is going to be related to the stubs that we have generated
    schema_pb2_grpc.add_TelefoniaServiceServicer_to_server(
        ClassForServiceServicer(), server)
    
    # We add the port where is going to be listening (we do not use security)
    server.add_insecure_port('[::]:50051')

    # Start the server
    server.start()
    
    print("Servidor gRPC corriendo en el puerto 50051...")
    server.wait_for_termination()

if __name__ == '__main__':

    # We call the function to create the server
    create_server()