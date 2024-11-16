import numpy as np

def detect_accident(accel_data):
    threshold = 5.0  # Example threshold for high G-forces
    if max(accel_data) > threshold:
        return True
    return False
