import RPi.GPIO as qq
import time

qq.setmode(qq.BCM)

led = 26
qq.setup(led, qq.OUT)

button = 13
qq.setup(button, qq.IN)
state = 1   
period = 0.2

while True:
    if qq.input(button):
        state = not state
        qq.output(led, state)
        time.sleep(period)
