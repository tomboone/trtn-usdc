import requests
import json
import settings
from flask import Flask, jsonify

app = Flask(__name__)


def account_balance(account):  # reusable function to get balance
    payload = json.dumps({
        'jsonrpc': '2.0',
        'id': 1,
        'method': 'getTokenAccountBalance',
        'params': [
            account
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request('POST', settings.url, headers=headers, data=payload)

    balance = json.loads(response.text)['result']['value']['uiAmount']

    return balance


@app.route('/')
def trtn_value():  # put application's code here
    trtnbal = account_balance(settings.trtnacct)
    usdcbal = account_balance(settings.usdcacct)
    trtvval = usdcbal/trtnbal

    return jsonify(
        name='trtn',
        value=trtvval
    )


if __name__ == '__main__':
    app.run()
