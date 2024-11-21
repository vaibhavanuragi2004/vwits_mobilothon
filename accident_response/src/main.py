from sensor_reader import read_sensor_data
from severity_analyzer import assess_severity
from voip_handler import initiate_voip_call
from notification_formatter import format_message

def main():
    sensor_data = read_sensor_data()
    severity = assess_severity(sensor_data)
    
    if severity > 0.7:  # Threshold for severe accidents
        message = format_message(sensor_data, severity)
        initiate_voip_call("+911234567890", message)  # Example emergency number
        print("Emergency authorities notified.")

if __name__ == "__main__":
    main()
