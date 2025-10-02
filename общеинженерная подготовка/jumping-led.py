import RPi.GPIO as qq
import time
qq.setmode(qq.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
qq.setup(leds, qq.OUT)

qq.output(leds, 0)


light_time = 0.2
while True:
    for i in leds:
        qq.output(i, 1)
        time.sleep(light_time)
        qq.output(i, 0)
    for i in reversed(leds):
        qq.output(i, 1)
        time.sleep(light_time)
        qq.output(i, 0)

