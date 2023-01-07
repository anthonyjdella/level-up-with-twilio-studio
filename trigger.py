import os

from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()


account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)


# Start a Flow Execution, aka Trigger our Studio Flow to run
def invoke_execution():
    execution = client.studio \
        .v2 \
        .flows(os.getenv('TWILIO_FLOW_SID')) \
        .executions \
        .create(
            from_=os.getenv('TWILIO_MSG_SRVC_SID'),
            to=os.getenv('MY_PERSONAL_NUMBER')
        )
    print(execution.sid)


invoke_execution()
