from flask import Flask
from flask import Response
from flask import request

from scheduler import schedule_message
from airtable import get_unique_numbers
from airtable import get_names_numbers


app = Flask(__name__)


@app.route("/v1/message/schedule", methods=["POST"])
def send_scheduled_texts_to_team_members():
    data = request.get_json()
    message = data.get("message")
    minutes_ahead = data.get("minutes-ahead")

    team_member_numbers = get_unique_numbers()

    for number in team_member_numbers:
        schedule_message(number, message, minutes_ahead)

    return Response('{"status": "message sent successfully"}', status=201, mimetype='application/json')


@app.route("/v1/users/names", methods=["GET"])
def get_team_member_names():
    current_caller = request.args.get('caller')

    team = get_names_numbers()

    for number,name in team.items():
        if number == current_caller:
            return Response('{"name": "' + name + '"}', status=201, mimetype='application/json')
        else:
            print(current_caller, " doesn't match ", number)

    return Response('{"status": "not allowed"}', status=401, mimetype='application/json')


@app.route("/v1/users/validate", methods=["POST"])
def validate_caller():
    data = request.get_json()
    caller = data.get("caller")

    if caller in get_names_numbers():
        return Response('{"status": "valid caller"}', status=201, mimetype='application/json')
    else:
        return Response('{"status": "invalid caller"}', status=401, mimetype='application/json')


'''
Get a Text Message Status

Invoke this from a Message API with the status_callback parameter (it takes a URL: localhost:3000/v1/message/status)
When the message status is updated, it will send a request to this endpoint

@app.route("/v1/message/status", methods=["POST"])
def status():
    message_sid = request.values.get('MessageSid', None)
    message_status = request.values.get('MessageStatus', None)
    to = request.values.get('To', None)
    print(message_sid, message_status)
    if message_status == "delivered":
        print("message was delivered!")
        return get_team_member_names(to)
    else:
        print("message was not delivered!")
        return Response('{"status": "message not sent"}', status=401, mimetype='application/json')
'''


if __name__ == "__main__":
    app.run(host='localhost', port=3000)
