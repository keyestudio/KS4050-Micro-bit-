'''
Theme: Rainwater monitoring
Function: OLED displays the amount of rainwater and the staem sensor controls the fan and atomization module
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
from oled_ssd1306 import *
import math
import music

# initialize and clear oled
initialize()  # initialize oled
clear_oled()  # clear oled

# Configuration parameters
RAIN_PIN = pin1
WET_VALUE = 1023
DRY_VALUE = 0

def map_value(value, in_min, in_max, out_min, out_max):
        """Linearly map the input values to the output range"""
    if in_max - in_min == 0:  # Prevent division by zero errors
        return out_min
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def get_rain_percentage():
    raw_value = RAIN_PIN.read_analog()
    percentage = map_value(raw_value, DRY_VALUE, WET_VALUE, 0, 100)
    return max(0, min(100, percentage)), raw_value

def get_rain_level(percentage):
    if percentage < 10:
        return "dry", 0
    elif percentage >= 10 and percentage < 20:
        return "slightly wet", 1
    elif percentage >= 20 and percentage < 40:
        return "wet", 2
    elif percentage >= 40 and percentage < 60:
        return "Very wet", 3
    else:
        return "hydrops", 4

def display_rain_info():
    percentage, raw_value = get_rain_percentage()
    level_text, level = get_rain_level(percentage)

    # Display on OLED
    clear_oled()
    add_text(0, 0, "Rainfall Monitor")
    add_text(0, 1, "Analog val: {}".format(raw_value))
    add_text(0, 2, "Humidity: {} %".format(percentage))
    add_text(0, 3, "State: {}".format(level_text))
    add_text(0, 4, "Class: {}".format(level))
    draw_screen()

    return percentage, level_text

while True:
    percentage, status = display_rain_info()

    # Display on the LED matrix and speaker plays different tones
    if percentage >= 10 and percentage < 20:
        display.show(Image("00000:00000:00900:00000:00000"))  # dot
        music.play("C3:1")  # speaker plays C3 tone
    elif percentage >= 20 and percentage < 40:
        display.show(Image("00000:00900:09990:00900:00000"))  # small circle
        music.play("C4:1")  # speaker plays C4 tone
    elif percentage >= 40 and percentage < 60:
        display.show(Image("00900:09990:99999:09990:00900"))  # middle circle
        music.play("C5:1")  # speaker plays C5 tone
    elif percentage >= 60:
        display.show(Image("09990:90009:90009:90009:09990"))  # large circle
        music.play("B5:1")  # speaker plays B5 tone
    else:
        display.show(Image("00000:00000:00000:00000:00000"))  # do not display any patterns
        music.reset()  # no tone
    sleep(1000)  # Update every second
