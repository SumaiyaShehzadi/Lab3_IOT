# Name: Sumaiya Shehzadi
# Reg:  22_NTU_CS_1376
# Home task: 2.1 Working with Neopixel and input button



print("starting of neopixel flashing ")          # just checking printing output

from machine import Pin
from neopixel import NeoPixel
import time

btn =Pin(0, Pin.IN, Pin.PULL_UP)    # same pin for physical esp32 s3 built in Boot buton
pin = Pin(33, Pin.OUT)              # set 48 for your physical esp32 s3  
neo = NeoPixel(pin, 1)              # create NeoPixel driver  for 1 pixel
while True:
    while(btn.value()==1):          # flashing of neopixel stopped when button is in pressed status
        neo[0] = (255, 0, 0)            # set the first pixel to red
        print("red")
    
        neo.write()                     # write data to all pixels
        time.sleep(.2)
        neo[0] = (0, 255, 0)            # set the first pixel to green
        print("red")
    
        neo.write()                     # write data to all pixels
        time.sleep(.2)       
        neo[0] = (0, 0, 255)            # set the first pixel to blue
        print("blue")
    
        neo.write()                     # write data to all pixels
        time.sleep(.2) 
    


# Task Questions:
# Upload the same code to a physical ESP32 S3:

# Run the code.
# Take a snapshot of Thonny.
# Record a short video of your physical device (change the pin from 33 to 48 for the physical device).
# Investigate the Neopixel color behavior:

# Why does the Neopixel always turn blue when the button is pressed?
The neopixel turns blue bcz the code cycle through the color in afixed red,green,blue .
since the loop run continusly as long as the button is pressed it quickly cycle to last color blue

# How can it be made to stop on different colors in real-time (e.g., sometimes red, sometimes green, sometimes blue)?
Detect button preses more prcisely
Only change the color when the button sttte changes from press to press
Change the color only once per press instead of looping contionously.
# Modify the code for button presses:

From machine import Pin
from neopixel import neopixel
import time 
import random

btn=Pin(0,Pin.in,pin\.pull-up)
pin=Pin(33,pin-out)
neo=NeoPixel(pin,1)

prev-btn-state=1

While True:
btn-stat=bt.value()
if prev-btn-state==1 and btn-state==0:
color=ranodm.choice([255,0,0),(0,255,0),(0,0,255)])
neo[0]=color
neo.write()
print(f"color:{color})
time.sleep(0.3)
prev-btn-state=btn_state



# Change the color after every 5 button presses.


if press-count==5:
    color-index=(color-index+1)%len(colors)
    neo[0]=color[color-index]
    neo.write()
    print(f'color.change to:{colors[color
    -index]}"")
    press-count=0
    time.sleep(0.3)



# Examine the result: Does the color change exactly after 5 presses, or is there abnormal behavior?
in most cases the color should change exactly after 5 pressesabnormal behaviour occur:
button bouncing caues mutiple trigger for one pressthe buttton is not fully released before the next preess

# If there is abnormal behavior, what could be the reason?
button debouncing issues
timing problem
Hardware glitch
# Make your own code modifications:
# Implement your own changes to the code.
improved debouncing
state cahnge Detection
Add short debounce checkingMaintained longer delay
from machine import Pin
from neopixel import NeoPixel
import time

btn = Pin(0, Pin.IN, Pin.PULL_UP)  # Button input
pin = Pin(33, Pin.OUT)             # NeoPixel data pin
neo = NeoPixel(pin, 1)             # Create NeoPixel driver for 1 pixel

press_count = 0       # Count button presses
prev_btn_state = 1    # Track previous button state
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
color_index = 0       # Index to track current color

while True:
    btn_state = btn.value()
    
    # Check for button press (transition from high to low)
    if prev_btn_state == 1 and btn_state == 0:
        time.sleep(0.05)  # Short debounce check
        if btn.value() == 0:  # Confirm button is still pressed
            press_count += 1
            print(f"Press count: {press_count}")
            
            # Change color after every 5 presses
            if press_count == 5:
                color_index = (color_index + 1) % len(colors)  # Cycle through colors
                neo[0] = colors[color_index]
                neo.write()
                print(f"Color changed to: {colors[color_index]}")
                press_count = 0  # Reset count
                
            time.sleep(0.3)  # Longer debounce delay
        
    prev_btn_state = btn_state  # Update button state



# Submit the link to your Wokwi project for all tasks (no hardware changes required for any task). Ensure all questions are answered in your own words, and the code is written in your own style.

# Most important: Do your own work. This is a viva-based home task.