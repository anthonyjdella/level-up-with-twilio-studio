import os
from datetime import datetime
from datetime import timedelta

from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()


account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

# Check the current time in UTC
print(datetime.utcnow())

# Scheduled message must be be sent in between 15 minutes (901 seconds) to 7 days in the future
sixteen_minutes_from_now = datetime.utcnow() + timedelta(minutes=16)
print(sixteen_minutes_from_now)


# Schedule a message to be sent at a fixed time
def schedule_message(body):
    message = client.messages \
        .create(
            messaging_service_sid=os.getenv('TWILIO_MSG_SRVC_SID'),
            to=os.getenv('MY_PERSONAL_NUMBER'),
            body=body,
            send_at=sixteen_minutes_from_now,
            schedule_type='fixed'
        )
    print(message.sid)


# Cancel a scheduled message
def cancel_message(message_sid):
    message = client.messages(message_sid) \
        .update(
            status='canceled'
        )
    print(message.status)


# def trigger_flow():
#     pass


# schedule_message("Good morning! Let's all stand up!")
