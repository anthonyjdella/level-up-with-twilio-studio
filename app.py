from flask import Flask
from scheduler import schedule_message


app = Flask(__name__)


@app.route("/sit-down", methods=["GET"])
def good_morning_sms():
    return schedule_message("Good morning! It's time for daily sit-down!", 16)


if __name__ == "__main__":
    app.run(host='localhost', port=3000)
