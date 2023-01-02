from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, this is automation using docker, kubernetes, jenkins and ArgoCD!!!!'
