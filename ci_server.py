from flask import Flask, request
import os
import json
import hmac
import hashlib

app = Flask(__name__)


@app.route('/', methods=['POST'])
def github_event():
    if request.headers.get('X-Github-Event') != 'push':
        return ''

    payload = json.loads(request.form.get('payload'))

    if payload.get('ref') != 'refs/heads/master':
        return ''

    hexa = hmac.new(os.environ.get('GITHUB_KEY'), json.dumps(
        request.form), hashlib.sha1).hexdigest()

    print(hexa)
    print(request.headers.get('X-Hub-Signature'))

    print(request.data)

    return ''
