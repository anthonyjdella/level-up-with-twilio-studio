import os
from datetime import datetime
from datetime import timedelta

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv


load_dotenv()


account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

# Check the current time in UTC
print(datetime.utcnow())


# Schedule a message to be sent at a fixed time
def schedule_message(to_number, body, minutes_ahead):
    try:
        message = client.messages \
            .create(
                messaging_service_sid=os.getenv('TWILIO_MSG_SRVC_SID'),
                to=to_number,
                body=body,
                send_at=minutes_from_now(minutes_ahead),
                schedule_type='fixed',
                # status_callback='https://ngrok.anthonydellavecchia.com/v1/message/status', \
                # This is the URL that Twilio will send a request to when the message status is updated
            )
        print(message.sid)
    except TwilioRestException as e:
        print(e)


# Scheduled message must be be sent in between 15 minutes (901 seconds) to 7 days in the future
def minutes_from_now(minutes_ahead):
    if (minutes_ahead > 15):
        print(datetime.utcnow() + timedelta(minutes=minutes_ahead))
        return datetime.utcnow() + timedelta(minutes=minutes_ahead)
    else:
        print("Message must be scheduled at least 15 minutes from now.")


# Utility function to cancel a scheduled message
def cancel_message(message_sid):
    try:
        message = client.messages(message_sid) \
            .update(
                status='canceled'
            )
        print(message.status)
    except TwilioRestException as e:
        print(e)


# cancel_message("SMXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

# schedule_message("+1XXXXXXXXXX", "Good morning! Let's all stand up!", 16)
