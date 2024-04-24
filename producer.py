import json
from kafka import KafkaProducer
from time import sleep

bootstrap_servers = ['localhost:9092']
topic = 'cleaned_data'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

with open('cleaned_data.json', 'r') as file:
    data = file.readlines()

for line in data:
    price_data = json.loads(line.strip())
    producer.send(topic, value=price_data)
    print('Data entry sent to Kafka:', price_data)
    sleep(1)  