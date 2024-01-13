from flask import Flask
import datetime

app = Flask(__name__)

x = datetime.datetime.now()


@app.route("/data")
def get_time():
    return {
        'Name': "geek",
        "Age": "22",
        "Date": x,
        "programming": "python"
    }


if __name__ == "__main__":
    app.run(debug=True)