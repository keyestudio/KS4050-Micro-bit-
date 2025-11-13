'''
Theme: PM2.5 dust detection
Function: OLED displays the amount of PM2.5 dust and the PM2.5 dust sensor controls the micro:bit 5*5 dot matrix, speaker and atomization module
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
from oled_ssd1306 import *
import music
import time

# initialize and clear oled
initialize()
clear_oled()

# Pin configuration
led_Pin = pin1
out_Pin = pin2

pin16.write_digital(1) # set P16 pin to high level

# Time parameter
delayTime = 280
delayTime2 = 40
offTime = 9680

def microsecond_delay(us):
    """Precise microsecond delay"""
    start = time.ticks_us()
    while time.ticks_diff(time.ticks_us(), start) < us:
        pass

while True:
    # Measurement sequence
    led_Pin.write_digital(0)      # LED OFF
    microsecond_delay(delayTime)   # 280μs

    dustVal = out_Pin.read_analog()  # Read the sensor

    microsecond_delay(delayTime2)  # 40μs
    led_Pin.write_digital(1)      # LED ON
    microsecond_delay(offTime)     # 9680μs

    # Calculation and display
    if dustVal > 36.455:
        # The exact same calculation formula
        voltage = dustVal / 1024.0
        pm25 = (voltage - 0.0356) * 120000 * 0.035

        # OLED displays detailed information
        add_text(0, 0, "PM2.5 dust: ") # Display the value of PM2.5 in the corresponding position of OLED
        add_text(0, 2, str(round(pm25)) + " ug/m3") # Display the value of PM2.5 in the corresponding position of OLED

        # Quality indication
        if pm25  > 500 :    # PM2.5 value > 500
            display.show(Image.SAD) # LED matrix displays a sad pattern
            music.play("E5:4")       # speaker plays E5 tone
            sleep(1000)
            pin16.write_digital(0) # set P16 pin to low level
            sleep(200)
            pin16.write_digital(1) # set P16 pin to high level
            sleep(3000)
            pin16.write_digital(0) # set P16 pin to low level
            sleep(200)
            pin16.write_digital(1) # set P16 pin to high level
            sleep(1000)
        else: # or
            display.show(Image.HAPPY) # LED matrix displays a happy pattern
            music.reset()             # no tone
            pin16.write_digital(1) # set P16 pin to high level
    else:
        print("Low value:", dustVal)
        display.show(Image.NO)

    # delay 0.2s
    sleep(200)
    clear_oled()   # clear OLED
