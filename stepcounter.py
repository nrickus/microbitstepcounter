# A basic step counter for the microbit using Micro Python (MU)
from microbit import *

#Define variable to record steps
steps = 0

while True:
    # Check to see if a step has been taken. If so, display a smile and increase the number of steps by 1
    if accelerometer.was_gesture('shake'):
        steps += 1
        display.show(Image.HAPPY)
        sleep(500)
        display.clear()
    # Check to see if button A has been pressed. If so, display the number of steps taken
    if button_a.is_pressed():
        string_steps = str(steps)
        display.show(string_steps)
        sleep(500)
        display.clear()
   


     