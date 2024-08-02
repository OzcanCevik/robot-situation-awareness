'''def recognize_situation(sensor_data):
    # State Recognition algorithms
    pass '''

def recognize_situation(sensor_data):
    # Basit bir durum tanıma
    if sensor_data["temperature"] > 25:
        return "hot"
    else:
        return "normal"


