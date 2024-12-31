# Crear imagen de servicio rest
cd /mnt/d/home-2/Documentos/master/cloud_computer/docker-practice/docker_rest

docker build -t rest:1.0.0 . 

# Crear imagen de servicio kafka
cd /mnt/d/home-2/Documentos/master/cloud_computer/docker-practice/docker_kafka_topics

docker build -t kafka-topics:1.0.0 .

# Crear imagen de gRPC
cd /mnt/d/home-2/Documentos/master/cloud_computer/docker-practice/docker_gRPC

docker build -t grpc:1.0.0 .
