import os
import json
import hmac
import hashlib

from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['POST'])
def github_event():
    if request.headers.get('X-Github-Event') != 'push':
        return ''

    raw_data = request.get_data()
    hex_string = hmac.new(os.environ.get('GITHUB_KEY'),
                          raw_data, hashlib.sha1).hexdigest()

    if hmac.compare_digest(request.headers.get('X-Hub-Signature'), 'sha1=' + hex_string):
        return ''

    payload = json.loads(request.form.get('payload'))

    if payload.get('ref') != 'refs/heads/master':
        return ''

    print('all good')

    return ''
