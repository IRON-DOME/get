import RPi.GPIO as qq
import time
qq.setmode(qq.BCM)

light = 26
qq.setup(light,qq.OUT)

pwm = qq.PWM(light, 200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)

    duty+= 1.0
    if duty > 100:
        duty = 0.0