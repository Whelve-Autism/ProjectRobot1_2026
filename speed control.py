# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, sleep
import tinybit

display.show(Image.HAPPY)


while True:
    tinybit.car_run(80, 70)
    sleep(5000)
    tinybit.car_run(225, 200)
    sleep(5000)

