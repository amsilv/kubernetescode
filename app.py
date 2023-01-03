from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, novo deploy, teste do git.v4'
