from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, periodo de estudos!!! hoje Deus vai me abençoar com coisas maravilhosas, amém!!!!!!'
