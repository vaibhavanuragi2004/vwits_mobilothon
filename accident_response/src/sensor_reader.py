import random

def read_sensor_data():
    """
    Simulates reading data from vehicle sensors.
    :return: Dictionary containing accelerometer, gyroscope, and GPS data.
    """
    return {
        "accelerometer": (random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)),
        "gyroscope": (random.uniform(-180, 180), random.uniform(-180, 180), random.uniform(-180, 180)),
        "gps": (28.7041, 77.1025)  # Example coordinates
    }
