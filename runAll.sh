#-----------------------------------------------
# Creacion de red
#-----------------------------------------------

docker network create inference-ai

#-----------------------------------------------
# Inciar contendores para el servidor de kafka
#-----------------------------------------------

# Iniciar zookeeper 
docker run --rm -d --name zookeeper --network inference-ai --network-alias zookeeper -e "ZOOKEEPER_CLIENT_PORT=2181"\
        -e "ZOOKEEPER_TICK_TIME=2000" \
        -v /mnt/d/home-2/Documentos/master/cloud_computer/docker-practice/docker_kafka_server/storage/zookeeper/data:/var/lib/zookeeper/data \
        -v /mnt/d/home-2/Documentos/master/cloud_computer/docker-practice/docker_kafka_server/storage/zookeeper/log:/var/lib/zookeeper/log \
         confluentinc/cp-zookeeper:7.8.0 

# Se pone un tiempo mientras se inicia el servidor de zookeeper
sleep 5

# Iniciar kafka 
docker run --rm -d --name kafka-server --network inference-ai --network-alias kafka -e "ZOOKEEPER_CLIENT_PORT=2181"\
        -e "KAFKA_BROKER_ID=1" \
        -e "KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181" \
        -e "KAFKA_LISTENERS=EXTERNAL_SAME_HOST://:29092,EXTERNAL_DIFFERENT_HOST://:29093,INTERNAL://:9092" \
        -e "KAFKA_ADVERTISED_LISTENERS=INTERNAL://kafka:9092,EXTERNAL_SAME_HOST://localhost:29092,EXTERNAL_DIFFERENT_HOST://192.168.5.242:29093" \
        -e "KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=INTERNAL:PLAINTEXT,EXTERNAL_SAME_HOST:PLAINTEXT,EXTERNAL_DIFFERENT_HOST:PLAINTEXT" \
        -e "KAFKA_INTER_BROKER_LISTENER_NAME=INTERNAL" \
        -e "KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1" \
        -e "KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0" \
        -e "KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1" \
        -e "KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1" \
        -e "KAFKA_CONFLUENT_LICENSE_TOPIC_REPLICATION_FACTOR=1" \
        -e "KAFKA_CONFLUENT_BALANCER_TOPIC_REPLICATION_FACTOR=1" \
        -p 29092:29092 \
        -p 29093:29093 \
        -v "/mnt/d/home-2/Documentos/master/cloud_computer/docker-practice/docker_kafka_server/storage/kafka/data:/var/lib/kafka/data" \
        -v "/mnt/d/home-2/Documentos/master/cloud_computer/docker-practice/docker_kafka_server/storage/kafka/secrets:/etc/kafka/secrets" \
         confluentinc/cp-kafka:7.8.0 

# Se pone un tiempo mientras se inicia el servidor de kafka
sleep 5

#-----------------------------------------------
# Inciar contendor kafka topics
#-----------------------------------------------

docker run --rm -d --name kafka-topics --network inference-ai --network-alias kafka-topics \
        -v "/mnt/d/home-2/Documentos/master/cloud_computer/docker-practice/models:/usr/local/app/models" \
        kafka-topics:1.0.0

#-----------------------------------------------
# Inciar contendor rest
#-----------------------------------------------

docker run --rm -d --name rest --network inference-ai --network-alias rest \
        -v "/mnt/d/home-2/Documentos/master/cloud_computer/docker-practice/models:/usr/local/app/models" \
        -p 8000:8000 \
        rest:1.0.0

#-----------------------------------------------
# Inciar contendor gRPC
#-----------------------------------------------

docker run --rm -d --name grpc --network inference-ai --network-alias grpc \
        -v "/mnt/d/home-2/Documentos/master/cloud_computer/docker-practice/models:/usr/local/app/models" \
        -p 50051:50051 grpc:1.0.0

