from kafka import KafkaConsumer
import json
import itertools
from collections import deque
from pymongo import MongoClient

mongo_uri = "mongodb://localhost:27017"
client = MongoClient(mongo_uri)

db = client['Approri']

# Select/Create collection (similar to a table)
collection = db['Frequent']


def generate_candidate_itemsets(itemsets, k):
    candidates = []
    if any(isinstance(item, (tuple, list)) for item in itemsets):
        itemsets = [item for sublist in itemsets for item in sublist]
    
    itemsets = set(itemsets)

    for subset in itertools.combinations(itemsets, k):
        candidates.append(subset)
    return candidates

def hash_bucket(pair, table_size):
    return sum(hash(item) for item in pair) % table_size

consumer = KafkaConsumer('cleaned_data',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

window_size = 100  
window = deque(maxlen=window_size)  

item_counts = {}
min_support = 5
frequent_itemsets_set = set()


table_size = 1000  # Size of the hash table
hash_table = [0] * table_size  # Initialize the hash table

for message in consumer:
    transaction_msg = message.value
    transaction1d = []
    new_items = set()
    items = transaction_msg.get("also_buy", [])
    items.append(transaction_msg.get("asin", ""))

    for item in items:
        item_counts[item] = item_counts.get(item, 0) + 1
        transaction1d.append(item)

    window.append(transaction1d)  # Add transaction to the sliding window

    # Process only the transactions within the sliding window
    transactions = list(window)

    # Counting frequent items for the PCY algorithm
    for transaction in transactions:
        for item, count in item_counts.items():
            if count >= min_support:
                frequent_itemsets_set.add(item)

    frequent_itemsets = list(frequent_itemsets_set)

    # Generate candidate pairs and count them using the PCY algorithm
    candidate_pairs = generate_candidate_itemsets(frequent_itemsets, 2)

    for transaction in transactions:
        for pair in candidate_pairs:
            if all(item in transaction for item in pair):
                bucket_index = hash_bucket(pair, table_size)
                hash_table[bucket_index] += 1

    # Find the most frequent pairs from the hash table
    frequent_pairs = []
    for pair in candidate_pairs:
        bucket_index = hash_bucket(pair, table_size)
        if hash_table[bucket_index] >= min_support:
            frequent_pairs.append(pair)

    # Print the most frequent pairs
    for pair in frequent_pairs:
        pair_str = ' '.join(pair)
        item_key = str(pair)   
        item_json = json.dumps({pair: 1})
        item_dict = json.loads(item_json)
        #collection.insert_one(item_dict)
        print(f"Frequent Pair: {pair_str}")
        
