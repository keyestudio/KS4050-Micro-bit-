'''
Theme: Earthquake detection alarm
Function: OLEDn displays information related to earthquake intensity and the microbit accelerometer controls a 5*5 dot matrix and speaker.
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
from oled_ssd1306 import *
import music

# initialize and clear oled
initialize()  # initialize oled
clear_oled()  # clear oled

def get_acceleration_strength():
    """
    Read the combined acceleration intensity of the accelerometer
    Return the magnitude of the total acceleration rate (unit: mg, milli-g)
    """
    # Read the three-axis acceleration values
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    # Calculate the synthetic acceleration (vector modulus)
    strength = (x**2 + y**2 + z**2) ** 0.5

    return strength

while True:
    strenght = get_acceleration_strength()  # Read the intensity detected by the accelerometer on the microbit board
    if strenght < 900 or strenght > 1200:    # When the intensity detected by the accelerometer is less than 900 or greater than 1200
       clear_oled()   # clear OLED
       add_text(0, 0, 'Earthquake Warning')  # Display the character string in the corresponding position of OLED
       add_text(0, 2, 'Earthquake Level: ')  # Display the character string in the corresponding position of OLED
       add_text(0, 4, str(int(strenght)))  # Display the value of strength in the corresponding position of OLED
       music.play("C4:1")   # speaker plays C4 tone
       display.show(Image.GHOST) # LED matrix displays a ghost pattern
    else: # or
       clear_oled()  # clear OLED
       display.clear() # Set the brightness of all LEDs to 0 (off)
       music.reset()  # no tone
    sleep(500)
