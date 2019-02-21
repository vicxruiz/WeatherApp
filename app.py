from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    user_age = getUserAge()
    return user_age

def getUserAge():

    return age

if __name__ == '__main__':
    app.run()

