import json

def save_memory(data, filename="data/memory.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_memory(filename="data/memory.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
