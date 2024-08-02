
### `memory.py` File


import json

def save_memory(data, filename="data/memory.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_memory(filename="data/memory.json"):
    with open(filename, 'r') as f:
        return json.load(f)


'''
```python
import json 
import os 

class Memory:
    def __init__(self, memory_file='data/memory.json'):
        self.memory_file = memory_file
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as file:
                return json.load(file)
        else:
            return {}

    def save_memory(self):
        with open(self.memory_file, 'w') as file:
            json.dump(self.memory, file)

    def remember(self, situation, response):
        self.memory[situation] = response
        self.save_memory()

    def recall(self, situation):
        return self.memory.get(situation, None)
'''
