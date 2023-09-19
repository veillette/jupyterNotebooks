"""
This code sets up the LED and the Adafruit Motor Kit, then enters an infinite loop. 
Within the loop, it alternately blinks the LED and moves the stepper motor one step backward with each LED blink.
The LED blink rate and the number of motor steps can be adjusted by modifying the DELAY and STEPS constants
"""

import board
import digitalio
import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

# Set up the LED on pin D13
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Initialize the Adafruit Motor Kit
kit = MotorKit(i2c=board.I2C())

# Define constants for motor control
DELAY = 0.001
STEPS = 1

# Create an infinite loop
while True:
    # Toggle the LED on
    led.value = True
    
    # Move the stepper motor one step backward
    for i in range(STEPS):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
        time.sleep(DELAY)

    # Toggle the LED off
    led.value = False
    time.sleep(DELAY)
