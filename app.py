from flask import Flask, request
from json import dumps
import logging

logging.basicConfig(filename='flask-app.log', level=logging.DEBUG,
                    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s %(lineno)s %(args)s")

app = Flask(__name__)


@app.route("/<path:path>", methods=['GET', 'POST'])
def profile(path):
    try:
        logging.info("Request URL: " + request.url +  # request.path +
                     "\nRequest path: " + path +
                     "\nRequest params: " + str(request.query_string) +
                     "\nRequest headers: " + str(list(request.headers)) +
                     "\nRequest body: " + dumps(request.get_json()))
    except Exception as er:
        logging.exception(str(er))
    if request.method == 'POST':
        pass
    return "<p>Hello, World!</p>"
