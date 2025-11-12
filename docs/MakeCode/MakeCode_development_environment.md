## 3.2.1 About MakeCode

⚠️ **The following instructions are applied for Windows system (in Google Chrome or Microsoft Edge browser) but can also serve as a reference if you are using a different system.**

**MakeCode programming:**

Open the online version of Makecode: [https://makecode.microbit.org/](https://makecode.microbit.org/)

MakeCode:

![Img](./media/A637.png)

In the code editing area, there are always two blocks, “**on start**” and “**forever**”. **After powering on/resetting, codes in “on start” runs once, while those in “forever” runs in a loop.**

Click “**JS JavaScript**” to check JavaScript language.

![Img](./media/A754.png)

Click the arrow to switch to “**Python**” language.

![Img](./media/A814.png)

**Select the language of the interface:**

![Img](./media/Animation-3.gif)

Detailed steps:

(1) Click settings:

![Img](./media/A301.png)

(2) Click “Language”:

![Img](./media/A302.png)

(3) Select a language you are familiar with. Here we set it to “English”.

![Img](./media/A303.png)

## 3.2.2 MakeCode Extensions

### 3.2.2.1 Add an Extension

⚠️ **We provide you with hexadecimal code files(.hex) of each projects. You can directly import one to MakeCode or build code blocks manually. For the latter method, library files need to be added.**

⚠️ **<span style="color: rgb(255, 76, 65);">Note:</span>** Search this link in the extension page: `https://github.com/keyestudio/pxt-environment-kit-master`

![Img](./media/Animation-4.gif)

Detailed steps:

1\. Open MakeCode and click ![Img](./media/A806.png)(settings) to enter “**Extensions**”.

![Img](./media/A842.png)

Or click “**Extensions**” above the **Advanced**.

![Img](./media/A900.png)

2\. Search for the key words or GitHub link of the extension you want to load.

![Img](./media/A909.png)

3\. Here search for: `https://github.com/keyestudio/pxt-environment-kit-master`. Click ![Img](./media/A3257.png) and you will see “**Environment-and-Science**”

![Img](./media/A306.png)

4\. Load it. 

![Img](./media/A3316.png)

5\. Loaded:

![Img](./media/A335.png)

### 3.2.2.2 Update/Delete Extensions

⚠️ **Under normal circumstances, once extensions are added, there is no need to delete them. The following part is only for learning how to delete unnecessary extensions.**

![Img](./media/Animation-4.gif)

Detailed step:

1\. Click “**JavaScript**” to switch to text code.

![Img](./media/A724.png)

2\. Click “**Explorer**”.

![Img](./media/A749.png)

3\. Find “**Environment-and-Science**” and click ![Img](./media/A813.png) to delete it.

![Img](./media/A824.png)

4\. “**Remove it**”.

![Img](./media/A727.png)

## 3.2.3 MakeCode Code Download

### 3.2.3.1 Import Code

Here we take “**heatbeat**” project as an example to introduce how to import code to MakeCode.

![Img](./media/Animation-2.gif)

Detailed steps:

1\. Connect the board to computer via USB cable.

![Img](./media/A800.png)

If the red LED on the back of the board is on, that means the board is powered. When your computer communicates with the main board via the USB cable, the yellow LED on it will flashes. 

Then micro:bit board will appear on your computer as a driver named “MICROBIT”. Please note that it is not an ordinary USB disk as shown below.

![Img](./media/A849.png)

2\. Open the MakeCode of Web version or Windows 10 APP for programming, and click “**Import**”.

![Img](./media/A956.png)

3\. “**Import File...**”

![Img](./media/A042.png)

4\. “**Choose File**”.

![Img](./media/A06.png)

5\. Choose the code file you want to open. Here we choose “**heartbeat.hex**”.

![Img](./media/A28.png)

6\. “**Go ahead √**” to import it to MakeCode.

![Img](./media/A149.png)

In addition, you can also directly drag the file into MakeCode.

![Img](./media/A202.png)

7\. Imported:

![Img](./media/A217.png)

### 3.2.3.2 Download Code (WebUSB)

If WebUSB of **Google Chrome**/**Microsoft Edge** is enabled, you can access your micro USB hardware device directly through the online webpage. Therefore, you may just click “**Download**” to download the code to micro:bit board.

![Img](./media/Animation.gif)

Detailed steps:

#### 3.2.3.2.1 Devices Pairing

1\. Connect the board to computer via USB cable.

![Img](./media/A951.png)

2\. Click “**...**” and “**Connect device**”.

![Img](./media/A028.png)

3\. “**Next**”.

![Img](./media/A046.png)

4\. “**Pair**”.

![Img](./media/A104.png)

5\. Select to the corresponding “**device**”, and “**Connect**”.

![Img](./media/A127.png)

6\. “**Done**”.

![Img](./media/A144.png)

#### 3.2.3.2.2 Download Program

After connection, click “**Download**”![Img](./media/A212.png) and it will change into ![Img](./media/A220.png).

![Img](./media/A232.png)

⚠️ **ATTENTION:**

If there is no device to choose from, please refer to the following link for troubleshooting:

[https://makecode.microbit.org/device/usb/webusb/troubleshoot](https://makecode.microbit.org/device/usb/webusb/troubleshoot)

If your micro:bit board needs to update its firmware, please refer to:

[https://microbit.org/guide/firmware/](https://microbit.org/guide/firmware/)

### 3.2.3.3 Download Code (non-WebUSB)

1\. Connect the board to computer via USB cable.

![Img](./media/A800.png)

If the red LED on the back of the board is on, that means the board is powered. When your computer communicates with the main board via the USB cable, the yellow LED on it will flashes. 

Then micro:bit board will appear on your computer as a driver named “MICROBIT”. Please note that it is not an ordinary USB disk as shown below.

![Img](./media/A849.png)

2\. If you import the code on another browser, please follow:

![Img](./media/Animations-1.gif)

Detailed steps:

① Click “**Download**” to store a “**.hex**” file (a format that can be read by micro:bit). After that, copy and paste it to micro:bit board. 

For Windows, you can also select it to “**Send to → MICROBIT**” to copy “**.hex**” to micro:bit. During this process, the yellow indicator on the back of the board will flash. When done, the light stops flashing and remains on.

![Img](./media/A319.png)

![Img](./media/A449.png)

Or directly drag “**.hex**” into MICROBIT.

![Img](./media/A341.png)

![Img](./media/A345.png)

② After uploading the code to micro: bit board, the on-board 5 x 5 LED matrix shows ![Img](./media/A903.png) and ![Img](./media/A910.png) in a loop.

![Img](./media/A22.png)

⚠️ **Tip 1:** For Windows 10 system, you can also choose MackCode Windows 10 APP. Click to [Get Windows 10 App](https://apps.microsoft.com/detail/9nmqdq2xzkwk?hl=en-gb&gl=CN) for programming, and then just click “**Download**” to save code in micro:bit board.

⚠️ **Tip 2:** Each time you program, the MICROBIT disk will automatically pop up and return, but the hexadecimal(**.hex**) file you have copied to it will not be displayed. The board only receives and runs the latest uploaded file(**.hex**) but will not store it!

