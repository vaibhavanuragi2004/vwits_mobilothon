from twilio.rest import Client

def initiate_voip_call(phone_number, message):
    """
    Initiates a VoIP call to emergency services with accident details.
    :param phone_number: Phone number to call.
    :param message: Alert message to convey.
    """
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)
    
    call = client.calls.create(
        twiml=f"<Response><Say>{message}</Say></Response>",
        to=phone_number,
        from_="your_twilio_number"
    )
    print(f"VoIP call initiated: {call.sid}")
