from sensor_interface import read_sensor_data
from situation_recognition import recognize_situation
from decision_making import make_decision
from reactions import react
from memory import save_memory, load_memory

def main():
    # Bellekten geçmiş verileri yükleyin
    memory = load_memory()
    
    # Sensör verilerini okuyun
    sensor_data = read_sensor_data()
    
    # Durumu tanımlayın
    situation = recognize_situation(sensor_data)
    
    # Karar verin
    decision = make_decision(situation)
    
    # Tepki verin
    react(decision)
    
    # Yeni durumu belleğe kaydedin
    memory.append({'situation': situation, 'decision': decision})
    save_memory(memory)

if __name__ == "__main__":
    main()
