'''
Theme: A multi-sensor OLED monitoring platform based on Micro:bit
Function: OLED displays the values of multiple sensors
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
from oled_ssd1306 import *
import math
import time

display.show(Image.HAPPY)  # LED matrix displays a happy pattern

# initialize and clear oled
initialize()
clear_oled()

# Hardware connection: PM2.5 dust sensor
out_Pin = pin2
led_Pin = pin9

# Hardware connection: steam sensor
Steam_PIN = pin1
WET_VALUE = 1023
DRY_VALUE = 0

# Initialize the ADC pin (the ultraviolet sensor is connected to pin0)
uv_sensor = pin0

# Time parameter
delayTime = 280
delayTime2 = 40
offTime = 9680

def map_value(value, in_min, in_max, out_min, out_max):
    """Linearly map the input values to the output range"""
    if in_max - in_min == 0:
        return out_min
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def get_rain_percentage():
    """Read the sensor and return the percentage of rainfall"""
    raw_value = Steam_PIN.read_analog()
    percentage = map_value(raw_value, DRY_VALUE, WET_VALUE, 0, 100)
    return max(0, min(100, percentage))

def read_uv_index():
    raw_value = uv_sensor.read_analog()
    if raw_value > 1023:
        raw_value = 1023
    elif raw_value < 0:
        raw_value = 0
    uvi = raw_value * (15.0 / 1023)
    return round(uvi, 1)

def microsecond_delay(us):
    """Precise microsecond delay"""
    start = time.ticks_us()
    while time.ticks_diff(time.ticks_us(), start) < us:
        pass

while True:
    # Measurement sequence
    led_Pin.write_digital(0)      # LED OFF
    microsecond_delay(delayTime)   # 280μs
    dustVal = out_Pin.read_analog()  # Read the PM2.5 dust sensor
    microsecond_delay(delayTime2)  # 40μs
    led_Pin.write_digital(1)      # LED ON
    microsecond_delay(offTime)     # 9680μs

    Lightintensity = display.read_light_level()
    Temperature = temperature()
    soundLevel = microphone.sound_level()
    rain_percent = get_rain_percentage()
    uv = read_uv_index()
    clear_oled()
    if button_a.is_pressed(): # if button_a.is pressed
        sleep(200)
        pin13.write_digital(1) # the fan is rotating.
        pin15.write_digital(0)
        sleep(200)
    else: # or
        pin13.write_digital(0) # the fan does not rotate.
        pin15.write_digital(0)
    if button_b.is_pressed(): # if button_b.is pressed
        pin16.write_digital(0) # the atomization module sprays water mist.
        sleep(200)
        pin16.write_digital(1)
        sleep(3000)
        pin16.write_digital(0)
        sleep(200)
        pin16.write_digital(1)
        sleep(1000)
    else: # or
        pin16.write_digital(1) # the atomization module does not spray water mist.

    add_text(0, 0, "Temper:")
    add_text(7, 0, str(int(Temperature)) + "C") # Display the Temperature value on the OLED
    add_text(0, 2, "UV:")
    add_text(3, 2, str(int(uv))) # Display the UV value on the OLED
    add_text(5, 2, " | Rain:")
    add_text(13, 2, str(int(rain_percent)) + "%") # Display the percentage of rainfall on the OLED
    add_text(0, 4, "Light:")
    add_text(6, 4, str(Lightintensity)) # Display the light intensity on the OLED
    add_text(9, 4, " | Sound:")
    add_text(18, 4, str(soundLevel)) # Display the noise intensity on the OLED
    # Calculation and display
    if dustVal > 36.455:
        # The exact same calculation formula
        voltage = dustVal / 1024.0
        pm25 = (voltage - 0.0356) * 120000 * 0.035

        # OLED displays detailed PM2.5dust value information.
        add_text(0, 6, "PM2.5dust:")
        add_text(10, 6, str(round(pm25)) + "ug/m3")
    else:
        print("Low value:", dustVal)
    sleep(500)