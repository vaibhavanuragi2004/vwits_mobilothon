import firebase_admin
from firebase_admin import messaging, credentials

cred = credentials.Certificate("path_to_your_firebase_credentials.json")
firebase_admin.initialize_app(cred)

def send_push_notification(vehicle_id):
    """
    Sends a push notification to the vehicle owner.
    :param vehicle_id: Unique ID of the vehicle.
    """
    message = messaging.Message(
        notification=messaging.Notification(
            title="Geofencing Alert",
            body=f"Unauthorized movement detected for vehicle {vehicle_id}.",
        ),
        topic="vehicle_alerts",
    )
    response = messaging.send(message)
    print(f"Push notification sent: {response}")
