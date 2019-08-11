from flask import Flask
from datetime import datetime
import _thread
import time 
import requests

app = Flask(__name__)





@app.route('/')
def homepage():
    print("-------LOG---------")
    return """HELLO WORLD"""

@app.route('/ping')
def ping():
    return """HI"""

@app.route('/log')
def log():
    f=open("log.txt", "r")
    return """{data}""".format(data=f.read())

@app.route('/thread')
def thread():
    print("MAIN")
    _thread.start_new_thread(keepalive)


def keepalive():
    print("THRED STARTED")
    while True:
        time.sleep(3)
        p=requests.get("https://ddl39.herokuapp.com/ping")
        print("KEEP ALIVE")
     

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

