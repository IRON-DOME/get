import RPi.GPIO as qq
import time
qq.setmode(qq.BCM)
led = 26
qq.setup(led, qq.OUT)
state = 0
period = 0.5
while True:
    qq.output(led, state)
    state = not state
    time.sleep(period)
    