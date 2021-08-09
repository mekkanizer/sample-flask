from flask import Flask, request
import logging

logging.basicConfig(filename='flask-app.log', level=logging.DEBUG,
                    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s %(lineno)s %(args)s")

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def profile():
    try:
        logging.info("Request URL: " + request.url +
                     "Request headers: " + str(list(request.headers)) +
                     "Request body" + str(list(request.body)))
    except Exception as er:
        logging.exception(str(er))
    if request.method == 'POST':
        return {
            "username": "Семён",
            "theme": "Luna"
        }
    return "<p>Hello, World!</p>"
