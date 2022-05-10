import logging

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    for i in range(100000):
        app.logger.error(f'my test log {i}')
    return 'Hello World!'

if __name__ == '__main__':
    app.run()