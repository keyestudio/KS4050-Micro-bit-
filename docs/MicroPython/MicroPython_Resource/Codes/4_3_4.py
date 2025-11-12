'''
Theme: Intelligent noise tester
Function: OLED displays the noise intensity, and the microbit microphone controls the number of 5*5 dot matrix on
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
from oled_ssd1306 import *

# initialize and clear oled
initialize()  # initialize oled
clear_oled()  # clear oled

# function to map any range of numbers to another range
def map(value, fromMin, fromMax, toMin, toMax):
    fromRange = fromMax - fromMin
    toRange = toMax - toMin
    valueScaled = float(value - fromMin) / float(fromRange)
    return toMin + (valueScaled * toRange)

# set of images for simple bar chart
graph5 = Image("99999:"
               "99999:"
               "99999:"
               "99999:"
               "99999")
graph4 = Image("00000:"
               "99999:"
               "99999:"
               "99999:"
               "99999")
graph3 = Image("00000:"
               "00000:"
               "99999:"
               "99999:"
               "99999")
graph2 = Image("00000:"
               "00000:"
               "00000:"
               "99999:"
               "99999")
graph1 = Image("00000:"
               "00000:"
               "00000:"
               "00000:"
               "99999")
graph0 = Image("00000:"
               "00000:"
               "00000:"
               "00000:"
               "00000")
allGraphs = [graph0, graph1, graph2, graph3, graph4, graph5]

# ignore first sound level reading
soundLevel = microphone.sound_level()
sleep(200)

while True:
    clear_oled()      # clear OLED
    soundLevel = microphone.sound_level() # Read the sound intensity detected by the microphone on the microbit board
    add_text(0, 0, "Acoustic Sound Level:")  # Display the character string in the corresponding position of OLED
    add_text(0, 2, str(soundLevel))  # Display soundLevel in the corresponding position of OLED
    # map sound levels from range 0-255 to range 0-5 for choosing graph image
    soundLevel1 = int(map(soundLevel, 0, 255, 0, 5))
    display.show(allGraphs[soundLevel1])
    sleep(1000)
