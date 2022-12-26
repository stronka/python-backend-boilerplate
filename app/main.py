from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello, world!")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
