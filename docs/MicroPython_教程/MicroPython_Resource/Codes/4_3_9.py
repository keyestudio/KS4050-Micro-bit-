'''
Theme: Fire detection and alarm
Function: OLED displays information related to whether a fire has occurred, and the flame sensor controls the speaker, fan, etc
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from oled_ssd1306 import *
from microbit import *
import math
import music

# initialize and clear oled
initialize()  # initialize oled
clear_oled()  # clear oled

# Configuration parameters
FIRE_A_PIN = pin1  # Connect the A pin of the flame sensor to P1 (analog input)
FIRE_D_PIN = pin9  # Connect the D pin of the flame sensor to P9 (digital input)
BIG_FIRE_VALUE = 0  # The minimum ADC value in the flame state
FIRELESS_VALUE = 1023  # The maximum ADC value in a flameless state

def map_value(value, in_min, in_max, out_min, out_max):
    """Linearly map the input values to the output range"""
    if in_max - in_min == 0:  # Prevent division by zero errors
        return out_min
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def get_fire_percentage():
    """Read the sensor and return the flame intensity"""
    raw_value = FIRE_A_PIN.read_analog()
    percentage = map_value(raw_value, FIRELESS_VALUE, BIG_FIRE_VALUE, 0, 100)
    return max(0, min(100, percentage)) # It is limited within the range of 0 to 100

while True:
    fire_percent = get_fire_percentage()  # Read the flame intensity and limit it within the range of 0 to 100
    D_val = FIRE_D_PIN.read_digital() # Read the digital value connected to pin9, and assign it to D_val
    clear_oled()
    if D_val == 0:  # if a flame is detected
       add_text(0, 0, "Have a fire")   # Display the character string on the OLED
       add_text(0, 2, "Fire Val: " + str(fire_percent) + "%") # Display the flame intensity on the OLED
       display.show(Image.SAD) # LED matrix displays a sad pattern
       music.play("E5:8")      # speaker plays E5 tone
       sleep(1000)
       pin2.write_analog(500) # set P2 pin to analog 500
       pin16.write_digital(0) # set P16 pin to digital 0
    else: # or
       add_text(0, 0, "No fire")
       sleep(200)
       display.show(Image.HAPPY)  # LED matrix displays a happy pattern
       music.reset()  # no tone
       pin2.write_analog(0)
       pin16.write_digital(0)
