from flask import Flask, request
import json
import hmac

app = Flask(__name__)


@app.route('/', methods=['POST'])
def github_event():
    if request.headers.get('X-Github-Event') != 'push':
        return ''

    payload = json.loads(request.form.get('payload'))

    if payload.get('ref') != 'refs/heads/master':
        return ''

    hexa = hmac.new(b'testisalaisuus', digestmod='sha1').hexdigest()

    print(hexa)
    print(request.headers.get('X-Github-Signature'))

    print(json.dumps(payload, indent=2))

    return ''
