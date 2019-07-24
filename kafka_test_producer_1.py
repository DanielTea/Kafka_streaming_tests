from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:29092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))



for e in range(1000):
    data = {'number' : str(e)+'test2'}
    producer.send('numtest2', value=data)
    print(e)
    sleep(5)