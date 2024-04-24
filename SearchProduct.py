from kafka import KafkaConsumer
import json
import nltk
from nltk.corpus import stopwords
import string

from pymongo import MongoClient

mongo_uri = "mongodb://localhost:27017"
client = MongoClient(mongo_uri)

db = client['SearchResult']

# Select/Create collection (similar to a table)
collection = db['Frequent']


consumer = KafkaConsumer('cleaned_data',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Get user input for specific category
search_category = input("Kindly search for your specific category: ")

# Preprocess search category
search_category_no_punctuation = search_category.translate(str.maketrans('', '', string.punctuation))
stop_words = set(stopwords.words('english'))
search_category_filtered = ' '.join([word.lower() for word in search_category_no_punctuation.split() if word.lower() not in stop_words])

# Loop through Kafka messages
for message in consumer:
    transaction_msg = message.value
    items = transaction_msg.get("category", "")
    asin = transaction_msg.get("asin", "")
    title = transaction_msg.get("title", "")
    
    # Check if search category is present in items
    #print(items)
    for item in items:
        # Preprocess item for comparison
        item_no_punctuation = item.translate(str.maketrans('', '', string.punctuation))
        item_filtered = ' '.join([word.lower() for word in item_no_punctuation.split() if word.lower() not in stop_words])
        if search_category_filtered in item_filtered:
            item_key = str(asin)   
            item_json = json.dumps({asin: title})
            item_dict = json.loads(item_json)
            collection.insert_one(item_dict)
            print("ASIN:", asin)
            print("Title:", title)
            break  # Break out of the loop if found
