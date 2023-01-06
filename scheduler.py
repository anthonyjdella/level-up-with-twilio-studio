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

# Schedule a message to be sent in between 15 minutes (901 seconds) to 7 days in the future
fifteen_minutes_from_now = datetime.utcnow() + timedelta(seconds=901)
print(fifteen_minutes_from_now)

# Schedule a message to be sent at a specific (fixed) time
message = client.messages \
    .create(
        messaging_service_sid=os.getenv('TWILIO_MSG_SRVC_SID'),
        to=os.getenv('MY_PERSONAL_NUMBER'),
        body='This is a scheduled message',
        send_at=fifteen_minutes_from_now,
        schedule_type='fixed'
    )
print(message.sid)

# Cancel a scheduled message
'''
message = client.messages('SMa3e29bf635f9b0eb8edda580c6feeeaa') \
    .update(status='canceled')

print(message.status)
'''
