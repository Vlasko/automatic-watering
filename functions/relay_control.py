# Standard Library Imports
from time import sleep

# Third Party Imports
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def setup(pin):
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

def on(pin):
    GPIO.output(pin, GPIO.HIGH)

def off(pin):
    GPIO.output(pin, GPIO.LOW)

def switch(time:int, pin):
    setup(pin)
    on(pin)
    sleep(time)
    off(pin)
