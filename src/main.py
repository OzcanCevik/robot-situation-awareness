from sensor_interface import read_sensor_data
from situation_recognition import recognize_situation
from decision_making import make_decision
from reactions import react 
from memory import save_memory, load_memory

def main():
    data = sensor_interface.read_sensor()
    print(data)

if __name__ == "__main__":
    main()


def main():
    print("Loading memory...")
    # Bellekten geçmiş verileri yükleyin
    memory = load_memory()
    print(f"Memory loaded: {memory}")

    print("Reading sensor data...")
    # Sensör verilerini okuyun
    sensor_data = read_sensor_data()
    print(f"Sensor data: {sensor_data}")

    print("Recognizing situation...")
    # Durumu tanımlayın
    situation = recognize_situation(sensor_data)
    print(f"Recognized situation: {situation}")

    print("Making decision...")
    # Karar verin
    decision = make_decision(situation)
    print(f"Decision made: {decision}")

    print("Reacting to decision...")
    # Tepki verin
    react(decision)

    print("Saving new memory state...")
    # Yeni durumu belleğe kaydedin
    memory.append({'situation': situation, 'decision': decision})
    save_memory(memory)
    print("Memory saved.")

if __name__ == "__main__":
    main()

# Mock the sensor_interface module
try:
    from sensor_interface import read_sensor_data
except ImportError:
    def read_sensor_data():
        print("Using mocked read_sensor_data")
        return "Simulated Sensor Data"

# Mock the situation_recognition module
try:
    from situation_recognition import recognize_situation
except ImportError:
    def recognize_situation(sensor_data):
        print(f"Using mocked recognize_situation with data: {sensor_data}")
        return "Simulated Situation"

# Mock the decision_making module
try:
    from decision_making import make_decision
except ImportError:
    def make_decision(situation):
        print(f"Using mocked make_decision with situation: {situation}")
        return "Simulated Decision"

# Mock the reactions module
try:
    from reactions import react
except ImportError:
    def react(decision):
        print(f"Using mocked react with decision: {decision}")

# Mock the memory module
try:
    from memory import save_memory, load_memory
except ImportError:
    def save_memory(memory):
        print(f"Using mocked save_memory with memory: {memory}")
        
    def load_memory():
        print("Using mocked load_memory")
        return []

def main():
    print("Loading memory...")
    # Bellekten geçmiş verileri yükleyin
    memory = load_memory()
    print(f"Memory loaded: {memory}")

    print("Reading sensor data...")
    # Sensör verilerini okuyun
    sensor_data = read_sensor_data()
    print(f"Sensor data: {sensor_data}")

    print("Recognizing situation...")
    # Durumu tanımlayın
    situation = recognize_situation(sensor_data)
    print(f"Recognized situation: {situation}")

    print("Making decision...")
    # Karar verin
    decision = make_decision(situation)
    print(f"Decision made: {decision}")

    print("Reacting to decision...")
    # Tepki verin
    react(decision)

    print("Saving new memory state...")
    # Yeni durumu belleğe kaydedin
    memory.append({'situation': situation, 'decision': decision})
    save_memory(memory)
    print("Memory saved.")

if __name__ == "__main__":
    main()
