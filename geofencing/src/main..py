from gps_tracker import is_within_boundary
from notification_handler import send_push_notification
from lockdown import activate_lockdown

def main(vehicle_id, current_location, authorized_boundary):
    if not is_within_boundary(current_location, authorized_boundary):
        send_push_notification(vehicle_id)
        activate_lockdown(vehicle_id)
        print("Unauthorized movement detected. Lockdown initiated.")

if __name__ == "__main__":
    vehicle_id = "VW12345"
    current_location = (28.7041, 77.1025)  # Example coordinates
    authorized_boundary = [(28.7, 77.1), (28.8, 77.2)]  # Boundary coordinates
    main(vehicle_id, current_location, authorized_boundary)
