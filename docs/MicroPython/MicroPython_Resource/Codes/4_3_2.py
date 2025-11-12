'''
Theme: Light intensity detector
Function: OLED displays the light intensity and the microbit light sensor controls the 5*5 dot matrix and speaker
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
from oled_ssd1306 import *
import music

val1 = Image("90909:""09990:""99999:""09990:""90909")  # Set pattern
val2 = Image("00000:""00900:""09990:""00900:""00000")  # Set pattern

# initialize and clear oled
initialize()  # initialize oled
clear_oled()  # clear oled

while True:
    clear_oled()  # clear OLED
    Lightintensity = display.read_light_level() # Read the light intensity detected by the microbit light sensor and assign it to the variable Lightintensity
    add_text(0, 0, 'Lightintensity:')  # Display the character string in the corresponding position of OLED
    add_text(16, 0, str(Lightintensity))  # Display Lightintensity in the corresponding position of OLED
    if Lightintensity >= 100: # when Light intensity > 100
       display.show(val1)   # LED matrix displays the set pattern1
       music.play("C5:1")   # speaker plays C5 tone
       sleep(50)
       music.play("D5:2")   # speaker plays D5 tone
       sleep(50)
       music.play("B5:4")   # speaker plays B5 tone
       sleep(50)
    elif Lightintensity > 0 and Lightintensity < 100:  # when 0 < Light intensity < 100
       display.show(val2)   # LED matrix displays the set pattern2
       music.play("C3:1")   # speaker plays C3 tone
    else: # or
       display.clear()   # Set the brightness of all LEDs to 0 (off)
       music.reset()     # no tone
    sleep(1000)
