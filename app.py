from flask import Flask, request
import logging

logging.basicConfig(filename='flask-app.log', level=logging.DEBUG)

app = Flask(__name__)


@app.route("/")
def profile():
    # logging.info("Request URL: " + request.url +
    #              "Request headers: " + request.headers +
    #              "Request body" + request.body)
    if request.method == 'POST':
        return {
            "username": "Семён",
            "theme": "Luna"
        }
    return "<p>Hello, World!</p>"
