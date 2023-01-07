from flask import Flask
from scheduler import schedule_message


app = Flask(__name__)


@app.route("/stand-up", methods=["GET"])
def good_morning_sms():
    print("Starting schedule!")
    schedule_message("Good morning! Let's all stand up!")
    print("Finished schedule!")
    return "Hello, world 2!"


if __name__ == "__main__":
    app.run(host='localhost', port=3000)
