#Code switches on and off LED on RaspberryPi using GPIO pins
#LED connected to GPIO 4 on the PI - pin number 7
#Check http://elinux.org/RPi_Low-level_peripherals for pin mapping

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

while 1:
        GPIO.output(7, True)
        time.sleep(1)
        GPIO.output(7, False)
        time.sleep(1)
