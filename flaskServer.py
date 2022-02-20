
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import time
from datetime import datetime
import RPi.GPIO as GPIO
import flask
from flask import Flask, render_template

# Create an app object of flask and tell flask where css etc. are located for html pages
app = Flask(__name__,
            static_url_path='',
            static_folder='templates/static',
            template_folder='templates')

# Define sensor ports
buzzer_pin = 2
pinMode(buzzer_pin,"OUTPUT")

# Define route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Runs code to turn on buzzer and serves html page
@app.route('/page2.html')
def page2():
    digitalWrite(buzzer_pin,1)
    time.sleep(2)
    digitalWrite(buzzer_pin,0)
    time.sleep(2)
    
    return render_template('page2.html')

# Define route for alarm history page
@app.route('/page1.html')
def page1():
    return render_template('page1.html')

# Puts sensors in original state to avoid crashes    
GPIO.cleanup()

# Runs server of localhost with port 8888
if __name__== "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
