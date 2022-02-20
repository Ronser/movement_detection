import grovepi
from grove_rgb_lcd import *
from grovepi import *
import time
from wia import Wia
from datetime import datetime
import RPi.GPIO as GPIO 

#initiate wia object and set access key for my device
wia = Wia()
wia.access_token = "YOUR_WIA_ACCESS_TOKEN"

# Define sensor ports and output modes D4
ultrasonic_ranger = 4
lastdistance = 0
led = 3
buzzer_pin = 2
pinMode(led,"OUTPUT")
pinMode(buzzer_pin,"OUTPUT")

#This function monitors for movement
def getReading():
    print ("Starting reading...")
    lastdistance = 0
    while True:
        try:
            # Read distance value from Ultrasonic
            distance = grovepi.ultrasonicRead(ultrasonic_ranger)
        
            # Checks if the distance has changed significantly
            if (distance - lastdistance) > 5: 
                
                #turn on the warning LED
                digitalWrite(led,1)
                #Display LCD warning message to intruder
                setText("Movement detected\nSystem alert!")
                setRGB(0,128,64)
                #Get the date for wia event data packet
                today = datetime.now()
                today = today.strftime('%m/%d/%Y')
                #Publish event to wia
                wia.Event.publish(name="Movement detected!", data="Movement detected at " + today)
                time.sleep(3)
                setText("Everwatch in operation")
                time.sleep(3)
                # Turn off LCD screen
                setRGB(0,0,0)
            else:
                # Ensure LED is off
                digitalWrite(led,0)
                
            #Set distance for next comparison   
            lastdistance = distance
        
        # Terminal info for errors    
        except KeyboardInterrupt:
            print ("You pressed a key")
        except IOError:
            print ("IO Error")

# Puts sensors in original state to avoid crashes            
GPIO.cleanup()

if __name__== "__main__":
    getReading()  
