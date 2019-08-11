from flask import Flask
from datetime import datetime
import threading 
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return """HELLO WORLD"""

@app.route('/ping')
def ping():
    return """HI"""


def keepalive():
    p=requests.get("https://ddl39.herokuapp.com/ping")    

if __name__ == '__main__':
    t1 = threading.Thread(target=keepalive)
    t1.start() 
    app.run(debug=True, use_reloader=True)

