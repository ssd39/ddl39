from flask import Flask
from datetime import datetime
import threading
import time 
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
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
        time.sleep(10000)
        p=requests.get("https://ddl39.herokuapp.com/ping")
        f = open("log.txt", "a")
        the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
        f.write("KEEP ALIVE SENT AT: {}".format(the_time))
        f.close()
     

if __name__ == '__main__':
    t1 = threading.Thread(target=keepalive)
    t1.start() 
    app.run(debug=True, use_reloader=True)

