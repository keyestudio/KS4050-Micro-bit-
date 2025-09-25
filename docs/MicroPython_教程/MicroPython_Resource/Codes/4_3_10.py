'''
Theme: Detection of flammable gas leakage
Function: OLED shows whether there is a flammable gas leak and the MQ2 analog gas sensor controls the speaker, fan, etc
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
Gas_A_PIN = pin1  # Connect the A pin of the MQ2 analog gas sensor to P1 (analog input)
Gas_D_PIN = pin9  # Connect the D pin of the MQ2 analog gas sensor to P9 (digital input)
GAS_VALUE = 1023  # The maximum ADC value in the presence of flammable gas (max amount of flammable gas)
GASLESS_VALUE = 0  # The minimum ADC value in the absence of flammable gas (non-flammable gas)

def map_value(value, in_min, in_max, out_min, out_max):
    """Linearly map the input values to the output range"""
    if in_max - in_min == 0:  # Prevent division by zero errors
        return out_min
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def get_gas_percentage():
    """Read the sensor and return the concentration of the analog gas MQ2"""
    raw_value = Gas_A_PIN.read_analog()
    percentage = map_value(raw_value, GASLESS_VALUE, GAS_VALUE, 0, 100)
    return max(0, min(100, percentage)) # It is limited within the range of 0 to 100

while True:
    gas_percent = get_gas_percentage() # Read the gas concentration and limit it within the range of 0 to 100
    D_val = Gas_D_PIN.read_digital() # Read the digital value connected to pin9, and assign it to D_val
    clear_oled()
    if D_val == 0:  # If gas is detected
       add_text(0, 0, "Gas leakage")   # Display the character string on the OLED
       add_text(0, 2, "Gas Val: " + str(gas_percent) + "%") # Display the gas concentration on the OLED
       display.show(Image.SAD) # LED matrix displays a sad pattern
       music.play("E5:8")      # speaker plays E5 tone
       sleep(1000)
       pin2.write_analog(500) # set P2 pin to analog 500
       pin16.write_digital(0) # set P16 pin to digital 0
    else: # or
       add_text(0, 0, "No gas leakage")
       sleep(200)
       display.show(Image.HAPPY)  # LED matrix displays a happy pattern
       music.reset()  # no tone
       pin2.write_analog(0)
       pin16.write_digital(0)
