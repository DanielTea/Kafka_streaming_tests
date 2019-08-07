#Docker Kafka / Zookeeper Test Project:

##How to use Step-by-Step:

Step 1: Download Wurstmeister/Kafka & Wurstmeister/Zookeeper Docker Containers

Step 2: Start Wurstmeister/Zookeeper Container, name the Host ```--hostname zookeeper```. Match Zookeeper  ports to  ```-p 2181:2181, -p 2888:2888, -p 3888:3888```

Step 3: Start Wurstmeister/Kafka with Environment Variables:

```
KAFKA_ZOOKEEPER_CONNECT = zookeeper:2181

KAFKA_ADVERTISED_PORT = 9092

KAFKA_ADVERTISED_LISTENERS = PLAINTEXT://kafka:9092, PLAINTEXT_HOST://localhost:29092

KAFKA_LISTENER_SECURITY_PROTOCOL_MAP = PLAINTEXT:PLAINTEXT, PLAINTEXT_HOST:PLAINTEXT

KAFKA_INTER_BROKER_LISTENER_NAME = PLAINTEXT

KAFKA_LISTENERS = PLAINTEXT://:9092, PLAINTEXT_HOST://:29092

KAFKA_CREATE_TOPICS = video-topic:7:1:compact, processed_video:1:1:compact
```

Step 4: Create links in Kafka -> ```zookeeper -> zookeeper``` and add ports ```-p 29092:29092```

Step 5: Create a Python environment in 3.6 and install the dependencies ```pip install -r requirements.txt```

Step 6: Now you can start, ```kafka_video_producer.py``` and ```emotion_recognition\emotion_engine.py``` and ```kafka_video_consumer.py```

## Things to read:
https://github.com/wurstmeister/kafka-docker

https://stackoverflow.com/questions/40326600/balancing-kafka-consumers/40327547

https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

https://kafka-python.readthedocs.io/en/1.1.0/apidoc/modules.html

