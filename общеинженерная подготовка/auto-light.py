import RPi.GPIO as qq
import time

qq.setmode(qq.BCM)

qw = 26
qq.setup(qw, qq.OUT)

ww = 6
qq.setup(ww, qq.IN)
while True:
    w = not qq.input(ww)
    qq.output(qw, w)    