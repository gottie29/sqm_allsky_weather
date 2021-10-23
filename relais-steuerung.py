import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

# Relay 1
#GPIO.setup(18, GPIO.OUT)
# Relay 2
GPIO.setup(23, GPIO.OUT)

try:
    while True:
        GPIO.output(23, GPIO.HIGH)
        print('Relay 1 ON')
        time.sleep(20)
        GPIO.output(23, GPIO.LOW)
        print('Relay 1 OFF')
        time.sleep(20)
        
finally:
    GPIO.cleanup()


GPIO.cleanup()
