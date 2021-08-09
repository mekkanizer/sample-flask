from flask import Flask, request, render_template
import logging

logging.basicConfig(filename='flask-app.log', level=logging.DEBUG)

app = Flask(__name__)


@app.route("/profile", methods=['GET', 'POST'])
def hello_world():
    logging.info("Request URL: " + request.url +
                 "Request headers: " + request.headers +
                 "Request body" + request.body)
    if request.method == 'POST':
        return {
            "username": "Семён",
            "theme": "Luna"
        }
    return "<p>Hello, World!</p>"
