import RPi.GPIO as qq
import time
qq.setmode(qq.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
qq.setup(leds, qq.OUT)
qq.output(leds, 0)

up = 9
down = 10
qq.setup(up, qq.IN)
qq.setup(down, qq.IN)

num = 0
sleep_time = 0.2
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
   
while True:
    if  qq.input(up) > 0:
        num += 1
        if num > 255:
            num -= 1
        if num < 0:
            num +=1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        for i in leds:
            if i == 1:
                qq.output(i, 1)
        else:qq.output(i, 0)


    
    if  qq.input(down) > 0:
        num -= 1
        if num > 255:
            num -= 1
        if num < 0:
            num +=1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        for i in leds:
            if i == 1:
                qq.output(i, 1)
        else:qq.output(i, 0)
