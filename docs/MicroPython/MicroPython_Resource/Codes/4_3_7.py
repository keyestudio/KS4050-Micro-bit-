'''
Theme: Air temperature and humidity regulation
Function: OLED displays temperature and humidity, XHT11 sensor controls the motor and the atomization module to regulate the environment temperature and humidity
Compiling IDE: MU 1.2.0
Author: https://docs.keyestudio.com
'''
# import related libraries
from microbit import *
from oled_ssd1306 import *
from DHT11 import *

# initialize and clear oled
initialize()
clear_oled()

sensor = DHT11(pin0)  # set temperature and humidity pins

# Add an initialization waiting time
display.show(Image.ALL_CLOCKS, wait=False, loop=True)
sleep(3000)  # Give the sensor a 3-second stabilization time
display.clear()

pin16.write_digital(1) # set P16 pin to high level

# Add a read counter
read_count = 0
last_valid_temp = 0
last_valid_humid = 0

while True:
    # Try reading multiple times
    for i in range(3):
        sensor.read() # read the temperature and humidity values
        if sensor.temp != 0 or sensor.humid != 0:
            break
        sleep(1000)
    T = sensor.temp  # store the temperature values in T
    H = sensor.humid  # store the humidity values in H

    # Check the validity of the data
    if T == 0 and H == 0 and read_count < 5:
        # The first few reads might be 0. Keep trying
        read_count += 1
        add_text(0, 0, "Initializing...")
        add_text(0, 2, "Attempt: " + str(read_count))
        sleep(1000)
        continue

    # If the data is valid, update the last valid value
    if T != 0 or H != 0:
        last_valid_temp = T if T != 0 else last_valid_temp
        last_valid_humid = H if H != 0 else last_valid_humid
        read_count = 10  # The mark has been successfully read

    # Use valid data (if the current value is 0, use the last valid value
    display_temp = T if T != 0 else last_valid_temp
    display_humid = H if H != 0 else last_valid_humid

    clear_oled()
    add_text(0, 0, "Temper: " + str(display_temp) + " C")   # Display the temperature value
    add_text(0, 2, "Humid: " + str(display_humid) + " %RH")   # Display the humidity value

    # control logic
    if display_temp > 30 or display_humid > 70:
        add_text(0, 4, "Cooling/Humidifying")
        pin2.write_analog(500)
        pin13.write_digital(0)
        sleep(2000)
        pin2.write_analog(0)
        pin13.write_digital(0)
        sleep(500)
        pin16.write_digital(0)
        sleep(3000)
        pin16.write_digital(1)
        sleep(1000)
        pin16.write_digital(0)
        sleep(3000)
        pin16.write_digital(1)
        sleep(1000)
    else:
        add_text(0, 4, "Normal State")
        pin2.write_analog(0)
        pin13.write_digital(0)
        pin16.write_digital(1)
    sleep(500)
