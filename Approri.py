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

consumer = KafkaConsumer('cleaned_data',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

window_size = 10  
window = deque(maxlen=window_size)  

item_counts = {}
min_support = 5
frequent_itemsets_set = set()

for message in consumer:
    transaction_msg = message.value
    transaction1d = []
    new_items=set()
    items = transaction_msg.get("also_buy", [])
    items.append(transaction_msg.get("asin", ""))
    
    for item in items:
        item_counts[item] = item_counts.get(item, 0) + 1
        transaction1d.append(item)

    window.append(transaction1d)  # Add transaction to the sliding window

    transactions = list(window)

    for transaction in transactions:
        for item, count in item_counts.items():
            if count >= min_support:
                frequent_itemsets_set.add(item)
                #print(f"Frequent item of size 1 is {item}")

    frequent_itemsets = list(frequent_itemsets_set)
    discarded = set()

    k = 1
    while k < 3:
        discarded_sets = {frozenset(item) for item in discarded}
        frequent_sets = {frozenset(item) for item in set(frequent_itemsets)}

        to_remove = {item for item in frequent_sets if any(subset in discarded_sets for subset in item)}

        frequent_itemsets = set(frequent_itemsets) - to_remove

        candidate_itemsets = generate_candidate_itemsets(frequent_itemsets, k+1)
        if not candidate_itemsets:
            break

        discarded = set(item_counts.keys()) - set(frequent_itemsets)

        item_counts = {}
        for transaction in transactions:
            for pair in candidate_itemsets:
                if all(item in transaction for item in pair):
                    item_counts[pair] = item_counts.get(pair, 0) + 1

        frequent_itemsets = []
        for item, count in item_counts.items():
            if count >= min_support:
                item_key = str(item)   
                item_json = json.dumps({item_key: count})
                frequent_itemsets_set.add(item)
                item_str = ' '.join(item)
                frequent_itemsets.append(item)
                item_dict = json.loads(item_json)
                collection.insert_one(item_dict)
                print(f"Frequent item of size {k+1} is {item_str}")

        k += 1
    transactions.clear()  
