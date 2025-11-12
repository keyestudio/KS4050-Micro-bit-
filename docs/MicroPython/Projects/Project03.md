### 4.3.3 Solar Ultraviolet Detector

#### 4.3.3.1 Overview

![Img](./media/top1.png)

The solar ultraviolet detector is a precision instrument used to measure the intensity of ultraviolet radiation from the sun. It detects ultraviolet(UV) radiation that is invisible to the human eye and quantify its intensity. Similar to light intensity detectors, they are also based on the photoelectric effect, but their core lies in the selective detection of ultraviolet rays.

In this project, the OLED will show the detected ultraviolet intensity in real time. When it exceeds a certain value, the speaker on the board will alarm, and the 5×5 LED matrix will display a pattern to serve as a warning.

The solar ultraviolet detector is widly used in almost all occasions that require the quantification of “ultraviolet light”, including tests of UV curing lamps and sunscreen products, ultraviolet phototherapy equipment, monitoring of ultraviolet sterilization lamps in water purification systems and air purification systems, etc.

![Img](./media/bottom1.png)

#### 4.3.3.2 Component Knowledge

![Img](./media/2top.png)

**Solar Ultraviolet Sensor**

![Img](./media/UV-sensor.png)

The ultraviolet sensor is used to detect ultraviolet rays, which is mainly composed of G365S01M based on semiconductor photodiodes. It can convert the UV radiation intensity in the environment into an analog voltage signal that can be read by a single-chip microcomputer (such as a micro:bit board). Its schematic diagram is as follows:

![Img](./media/UV.png)

Photoelectric conversion: When the ultraviolet photodiode inside the sensor is exposed to ultraviolet light, it generates an extremely weak current (proportional to the UV intensity).

Current amplification: This weak current is amplified by the internally integrated operational amplifier.

Signal output: The amplified signal directly outputs an analog voltage from a pin. The voltage value is usually between 0V and 1V (under 3.3V power supply). The stronger the UV intensity is, the higher the voltage will be.

**Parameters:**

- Operating voltage: DC 5V
- Peak response wavelength: 355nm (λmax)
- Peak responsivity (355nm) : 0.18A/W (Rmax)
- Spectral response range: 220~370nm
- UV/visible light responsivity ratio(Rmax/R400nm): > ![Img](media/103.png)(VB)

**Microbit 5×5LED Matrix**

![Img](./media/j101.png)

The LED matrix of micro:bit board contains 25 LEDs in a grid. We can control a certain LED by integrating its position value into the test code. Theoretically, we can turn on many LEDs at the same time to show patterns, digits and scrolling characters.

![Img](./media/2bottom.png)

#### 4.3.3.3 Required Components

| ![Img](./media/microbitV2.png)| ![Img](./media/ExpansionBoard.png)  |![Img](./media/OLED.png) |
| :--: | :--: | :--: |
|   micro:bit V2 main board ×1   |        micro:bit shield ×1         |           OLED display ×1           |
|![Img](./media/UV-sensor1.png)|![Img](./media/usb.png) |![Img](./media/4pin.png)|
|     ultraviolet sensor ×1      |         micro USB cable×1          | 4 pin wire(black-red-blue-green) ×1 |
|![Img](./media/3pin.png)|![Img](./media/batterycase.png)|![Img](./media/AAbattery.png)|
|         3 pin wire ×1          |         battery holder ×1          |  AA battery(**self-prepared**) ×6   |

#### 4.3.3.4 Wiring Diagram

⚠️ **When wiring, please pay attention to the wire color.**

| OLED display | wire color | micro:bit shield pin | micro:bit board pin |
| :----------: | :--------: | :------------------: | :-----------------: |
|     GND      |   black    |          G           |          G          |
|     VCC      |    red     |          V2          |          V          |
|     SDA      |    blue    |          20          |         P20         |
|     SCL      |   green    |          19          |         P19         |

| ultraviolet sensor | wire color | micro:bit shield pin | micro:bit board pin |
| :----------------: | :--------: | :------------------: | :-----------------: |
|         G          |   black    |          G           |          G          |
|         V          |    red     |          V2          |          V          |
|         S          |   yellow   |          1           |         P1          |

![Img](./media/couj3.png)

#### 4.3.3.5 Code Flow

![Img](./media/flow-chart-03.png)

#### 4.3.3.6 Test Code

⚠️ **<span style="color: rgb(255, 76, 65);">Tip 1: Before downloading the code to the Microbit board, please import the “oled_ssd1306” library refering to </span>** “[Import Library on MU](https://docs.keyestudio.com/projects/KS4050/en/latest/docs/MicroPython/MU_development_environment.html#import-library-on-mu)” .

⚠️ **Tip 2: The threshold 5 in the if() condition can be modified according to the actual situation.**

**Complete code:**

```Python
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
    # Read the analog value (0-1023 corresponds to 0-5.0V)
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
```

![Img](./media/line1.png)

**Brief explanation:**

① Import libraries of microbit, oled_ssd1306, music and math.

```Python
from microbit import *
from oled_ssd1306 import *
import music
import math
```

② Initialize OLED pixels, clear the OLED.

```Python
initialize()  # initialize oled
clear_oled()  # clear oled
```

③ Initialize the pin of the solar ultraviolet sensor.

```Python
uv_sensor = pin1
```

④ Define the sub-function of ultraviolet value detected by the sensor.

```Python
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
```

⑤ Read the ultraviolet value of the sensor and display it on the OLED.

```Python
uv = read_uv_index() # Read the ultraviolet intensity level detected by the ultraviolet sensor
add_text(0, 0, "UV Intensity:")  # Display the character string in the corresponding position of OLED
add_text(14, 0, str(int(uv)))  # Display Ultraviolet intensity level in the corresponding position of OLED
```

⑥ Judgement statement: if()...else...

When the detected ultraviolet intensity of sunlight is greater than or equal to 5, the 5×5LED matrix displays ![Img](./media/ab1.png) and ![Img](./media/ab2.png), and the speaker alarms. Or else, the matrix shows ![Img](./media/ab3.png) and the speaker does not alarm.

```Python
if uv >= 5:    # when uv level >=5
   display.show(Image.NO)    # LED matrix displays the no pattern
   music.play("B5:4")        # speaker plays B5 tone
   sleep(100)
   music.play("C5:4")        # speaker plays C5 tone
   display.show(Image.SAD)   # LED matrix displays the sad pattern
   sleep(100)
else: # or
   display.show(Image.HAPPY)  # LED matrix displays the happy pattern
   music.reset()              # no tone
```

⑦ Delay 1000ms(1s).

```Python
sleep(1000)
```

#### 4.3.3.7 Test Result

![Img](./media/4top.png)

After wiring up and power on by micro USB cable, connect to external power(6 AA batteries) to ensure sufficient power supply, and click “<span style="color: rgb(255, 76, 65);">Flash</span>” to download the code to micro:bit board.

![Img](./media/A125.png)

After uploading test code, press the reset button on the back of micro:bit.

![Img](./media/A455.png)

⚠️ **Note:** Test environment for ultraviolet sensor: Midday sunlight (10:00-14:00); Avoid shading; Directly face the sensor to the sun.

The OLED shows the detected ultraviolet intensity in real time. When the detected ultraviolet intensity of sunlight is greater than or equal to 5, the 5×5 LED matrix displays ![Img](./media/ab1.png) and ![Img](./media/ab2.png), and the speaker alarms. Or else, the matrix shows ![Img](./media/ab3.png) and the speaker does not alarm.

![Img](./media/dongtu-3.gif)

⚠️ **Note: The building blocks in the experiment are not included in this kit.**

<span style="color: rgb(0, 209, 0);">(**Tip:** If no result is observed, please press the reset button of the micro:bit board.)</span>

![Img](./media/4bottom.png)
