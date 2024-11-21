import numpy as np

def assess_severity(sensor_data):
    """
    Analyzes the severity of an accident based on sensor data.
    :param sensor_data: Dictionary with sensor readings.
    :return: Severity score (0 to 1).
    """
    accel_magnitude = np.linalg.norm(sensor_data["accelerometer"])
    return min(accel_magnitude / 10, 1)  # Normalizing severity to 0-1 scale
