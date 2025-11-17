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
graph5 = Image("99999:""99999:""99999:""99999:""99999")
graph4 = Image("00000:""99999:""99999:""99999:""99999")
graph3 = Image("00000:""00000:""99999:""99999:""99999")
graph2 = Image("00000:""00000:""00000:""99999:""99999")
graph1 = Image("00000:""00000:""00000:""00000:""99999")
graph0 = Image("00000:""00000:""00000:""00000:""00000")

allGraphs = [graph0, graph1, graph2, graph3, graph4, graph5]

# ignore first sound level reading
# soundLevel = microphone.sound_level()
# sleep(100)

while True:
    # map sound levels from range 0-255 to range 0-5 for choosing graph image
    soundLevel = int(map(microphone.sound_level(), 0, 255, 0, 5))
    display.show(allGraphs[soundLevel])
    clear_oled() # clear OLED
    add_text(0, 0, "Acoustic Sound Level:")  # Display the character string in the corresponding position of OLED
    add_text(0, 2, str(microphone.sound_level()))  # Display soundLevel in the corresponding position of OLED
    sleep(200)
