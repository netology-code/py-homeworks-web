#!/usr/bin/env python
import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    name = os.getenv('ADMINAME', 'Def')
    return f'Hello {name}!'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
