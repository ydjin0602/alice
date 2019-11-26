import json
import logging
from flask import Flask, request


app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)


@app.route("/", methods=['POST'])
def main():
    logging.info('Request: %r', request.json)
    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }
    response['response']['text'] = 'Да'
    logging.info('Response: %r', response)
    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )
