"""
Theme: smart temperature control fan
Function: OLED displays the temperature value and the microbit temperature sensor controls the on and off of the fan
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
"""
# import related libraries
from microbit import *
from oled_ssd1306 import *

display.show(Image.HAPPY)  # LED matrix displays a happy pattern

# initialize and clear oled
initialize()
clear_oled()

while True:
    clear_oled()  # clear OLED
    Temperature = temperature()  # Read microbit temperature sensor
    add_text(0, 0, "Temperature:")  # Display the character string in the corresponding position of OLED
    add_text(13, 0, str(Temperature) + " C")  # Display temperature in the corresponding position of OLED
    if Temperature > 33:  # when Temperature > 33℃, fan rotates
       add_text(0, 2, "Fan on")  # Display the character string in the corresponding position of OLED
       pin2.write_analog(500)  # set P2 pin to analog 500
       pin16.write_analog(0)  # set P16 pin to analog 0
    else:  # or fan does not work
       add_text(0, 2, "Fan off")  # Display the character string in the corresponding position of OLED
       pin2.write_analog(0)  # set P2 pin to analog 0
       pin16.write_analog(0)  # set P16 pin to analog 0
    sleep(1000)
