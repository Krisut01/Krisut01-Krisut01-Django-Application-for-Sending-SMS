from twilio.rest import Client
from django.conf import settings

def send_sms(recipient, message):
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            to=recipient,
            from_=settings.TWILIO_PHONE_NUMBER,
            body=message,
        )
        return {"status": "Sent", "sid": message.sid}
    except Exception as e:
        return {"status": "Failed", "error": str(e)}
