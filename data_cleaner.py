import json

def batch_generator(file_path, batch_size):
    with open(file_path, 'r') as infile:
        batch = []
        for line in infile:
            batch.append(json.loads(line))
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

def process_batch(batch):
    processed_batch = [{"also_buy": item.get("also_buy", []), "asin": item.get("asin", ""), "category": item.get("category",""),"title": item.get("title","") } for item in batch]
    return [json.dumps(entry) for entry in processed_batch]

batch_size = 10
file_path = 'Sampled_Amazon_eta.json'
output_file = 'cleaned_data.json'

with open(output_file, 'w') as outfile:
    for batch in batch_generator(file_path, batch_size):
        processed_batch = process_batch(batch)
        for entry in processed_batch:
            outfile.write(entry + '\n')
