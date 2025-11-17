### 4.3.4 Smart Noise Tester

#### 4.3.4.1 Overview

![Img](./media/top1.png)

The smart noise tester, also known as the sound level meter or decibel meter, is used to detect noise. Noise is classified into different levels, and the microphone on the micro:bit will detect its intensity in the environment in real time. According to the levels, micro:bit divides it into several grades.

In this project, the OLED display will show the current noise level in real time, and the 5×5LED matrix will light up/turn off some LED according to the noise level.

This kind of device has significantly lowered the technical threshold and cost of noise monitoring, so is widely applied to environment noise monitoring, occupational health and safety, construction sites, and entertainment venues, etc.

![Img](./media/bottom1.png)

#### 4.3.4.2 Component Knowledge

![Img](./media/2top.png)

**Microbit Microphone**

![Img](./media/j1101.png)

The micro:bit V2 board is built with a microphone which detects sounds and audio signals. The microphone is placed on the top of the board (the small hole, which is used for picking up ambient sound signals, and an LED indicator is next to the hole). The chip that controls and handles the microphone is located on the back of the board.

When using, simply place the micro:bit board face up.

![Img](./media/j1113.png)

When the board detects sound, the microphone LED indicator lights up.

![Img](./media/j1112.png)

![Img](./media/2bottom.png)

#### 4.3.4.3 Required Components

| ![Img](./media/microbitV2.png)| ![Img](./media/ExpansionBoard.png)  |![Img](./media/OLED.png) |
| :--: | :--: | :--: |
|    micro:bit V2 main board ×1    |         micro:bit shield ×1         |         OLED display ×1         |
|![Img](./media/usb.png) |![Img](./media/4pin.png)|![Img](./media/batterycase.png)|
|        micro USB cable ×1        | 4 pin wire ×1 |        battery holder ×1        |
|![Img](./media/AAbattery.png)| | |
|AA battery(**self-prepared**) ×6| | |

#### 4.3.4.4 Wiring Diagram

⚠️ **When wiring, please pay attention to the wire color.**

| OLED display | wire color | micro:bit shield pin | micro:bit board pin |
| :----------: | :--------: | :------------------: | :-----------------: |
|     GND      |   black    |          G           |          G          |
|     VCC      |    red     |          V2          |          V          |
|     SDA      |    blue    |          20          |         P20         |
|     SCL      |   green    |          19          |         P19         |

![Img](./media/couj4.png)

#### 4.3.4.5 Code Flow

![Img](./media/flow-chart-04.png)

#### 4.3.4.6 Test Code

⚠️ **<span style="color: rgb(255, 76, 65);">Tip 1: Before downloading the code to the Microbit board, please import the library file “oled_ssd1306\.py” refering to </span>** “[Import Library on MU](https://docs.keyestudio.com/projects/KS4050/en/latest/docs/MicroPython/MU_development_environment.html#import-library-on-mu)” .

![Img](./media/WPSA1.png)

**Complete code:**

```Python
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
```

![Img](./media/line1.png)

**Brief explanation:**

① Import libraries of microbit and oled_ssd1306.

```Python
from microbit import *
from oled_ssd1306 import *
```

② Initialize OLED pixels, clear the OLED.

```Python
initialize()  # initialize oled
clear_oled()  # clear oled
```

③ Define a map sub-function (to map any number range to another).

```Python
def map(value, fromMin, fromMax, toMin, toMax):
    fromRange = fromMax - fromMin
    toRange = toMax - toMin
    valueScaled = float(value - fromMin) / float(fromRange)
    return toMin + (valueScaled * toRange)
```

④ Define a set of simple bar graph images.

```Python
graph5 = Image("99999:""99999:""99999:""99999:""99999")
graph4 = Image("00000:""99999:""99999:""99999:""99999")
graph3 = Image("00000:""00000:""99999:""99999:""99999")
graph2 = Image("00000:""00000:""00000:""99999:""99999")
graph1 = Image("00000:""00000:""00000:""00000:""99999")
graph0 = Image("00000:""00000:""00000:""00000:""00000")

allGraphs = [graph0, graph1, graph2, graph3, graph4, graph5]
```

⑤ Map the sound value range of 0-255 to 0-5 of the selected graphic image.

```Python
soundLevel = int(map(microphone.sound_level(), 0, 255, 0, 5))
display.show(allGraphs[soundLevel])
```

⑥ Read the detected value and display it on the OLED.

```Python
clear_oled() # clear OLED
add_text(0, 0, "Acoustic Sound Level:")  # Display the character string in the corresponding position of OLED
add_text(0, 2, str(microphone.sound_level()))  # Display soundLevel in the corresponding position of OLED
sleep(200)
```

#### 4.3.4.7 Test Result

![Img](./media/4top.png)

After wiring up and power on by micro USB cable, connect to external power(6 AA batteries) to ensure sufficient power supply, and click “<span style="color: rgb(255, 76, 65);">Flash</span>” to download the code to micro:bit board.

![Img](./media/A126.png)

After uploading test code, press the reset button on the back of micro:bit.

![Img](./media/A455.png)

Blow air (or make a very loud noise) into the microphone on the Microbit board (⚠️ **<span style="color: rgb(255, 76, 65);">special reminder: Blowing air has a more obvious effect</span>**), and the OLED display will show real-time information related to air blowing (or noise) intensity, allowing users to intuitively understand the intensity of the air blowing (or noise). Meanwhile, the 5×5LED dot matrix screen on the Microbit board will gradually increase or decrease the number of rows of LED lights on the screen according to the intensity of the air blowing (or noise), achieving the effect of reminding the intensity of the air blowing (or noise)

![Img](./media/dongtu-4.gif)

⚠️ **Note: The building blocks in the experiment are not included in this kit.**

<span style="color: rgb(0, 209, 0);">(**Tip:** If no result is observed, please press the reset button of the micro:bit board.)</span>

![Img](./media/4bottom.png)
