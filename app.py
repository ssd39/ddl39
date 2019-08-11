from flask import Flask
from datetime import datetime
import threading
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




def keepalive():
    while True:
        time.sleep(10)
        p=requests.get("https://ddl39.herokuapp.com/ping")
        print("KEEP ALIVE")
     

if __name__ == '__main__':
    t1 = threading.Thread(target=keepalive)
    t1.start() 
    app.run(debug=True, use_reloader=True)

