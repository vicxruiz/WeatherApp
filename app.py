from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! I think it is about that time!!!!'


if __name__ == '__main__':
    app.run()

