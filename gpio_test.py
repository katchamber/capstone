import RPi.GPIO as GPIO
import time #import sleep

#******************
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

GPIO.output(4, GPIO.HIGH)
time.sleep(10)
GPIO.output(4, GPIO.LOW)


