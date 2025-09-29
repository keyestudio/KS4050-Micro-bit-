'''
Theme: Solar ultraviolet detector
Function: OLED displays the intensity of ultraviolet rays and the ultraviolet sensor controls the 5*5 dot matrix and speaker
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
from oled_ssd1306 import *
import music
import math

# initialize and clear oled
initialize()  # initialize oled
clear_oled()  # clear oled

# Initialize the ADC pin (the ultraviolet sensor is connected to pin1)
uv_sensor = pin1

def read_uv_index():
    # Read the analog value (0-1023 corresponds to 0-3.3V)
    raw_value = uv_sensor.read_analog()
    # Make sure the value is within the valid range
    if raw_value > 1023:
        raw_value = 1023
    elif raw_value < 0:
        raw_value = 0
    # Map to the ultraviolet index range of 0 to 15
    # The mapping range can be adjusted according to the actual characteristics of the sensor
    uvi = raw_value * (15.0 / 1023)

    return round(uvi, 1)

while True:
    clear_oled()   # clear OLED
    uv = read_uv_index() # Read the ultraviolet intensity level detected by the ultraviolet sensor
    add_text(0, 0, "UV Intensity:")  # Display the character string in the corresponding position of OLED
    add_text(14, 0, str(int(uv)))  # Display Ultraviolet intensity level in the corresponding position of OLED
    if uv >= 3:    # when uv level >=3
       display.show(Image.NO)    # LED matrix displays the no pattern
       music.play("B5:4")        # speaker plays B5 tone
       sleep(100)
       music.play("C5:4")        # speaker plays C5 tone
       display.show(Image.SAD)   # LED matrix displays the sad pattern
       sleep(100)
    else: # or
       display.show(Image.HAPPY)  # LED matrix displays the happy pattern
       music.reset()              # no tone
    sleep(1000)
