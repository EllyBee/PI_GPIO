#Code switches on LED when button is pressed on RaspberryPi using GPIO pins
#LED connected to GPIO 4 on the PI - pin number 7
#Button connected one one side to GPIO 17 on the PI - pin number 11 with a 10k resistor
#to GND. Other side connected to 3v.
#Check http://elinux.org/RPi_Low-level_peripherals for pin mapping
#Code based on https://docs.google.com/file/d/0B2-00drKdqF0V09YSHgxcTEtelk/edit?pli=1

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.IN)

while 1:
        if GPIO.input(11):
                GPIO.output(7, True)
        else:
                GPIO.output(7, False)