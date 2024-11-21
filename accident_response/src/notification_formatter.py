def format_message(sensor_data, severity):
    """
    Formats an alert message based on accident severity and location.
    :param sensor_data: Dictionary containing GPS and other data.
    :param severity: Severity score of the accident.
    :return: Formatted string message.
    """
    gps_location = sensor_data["gps"]
    return (f"Accident detected! Severity: {severity:.2f}. "
            f"Location: Latitude {gps_location[0]}, Longitude {gps_location[1]}. "
            "Immediate assistance required.")
