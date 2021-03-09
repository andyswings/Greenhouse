#!/usr/bin/python3

import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

def soilsensor1():
    value = adc.read_adc(0, gain=GAIN)
    return value

def soilsensor2():
    value = adc.read_adc(1, gain=GAIN)
    return value

def soilsensor3():
    value = adc.read_adc(2, gain=GAIN)
    return value

def soilsensor4():
    value = adc.read_adc(3, gain=GAIN)
    return value



def main():
    try:
        soilsensor1()
        soilsensor2()
        soilsensor3()
        soilsensor4()
    except KeyboardInterrupt:
        print("Exiting")

if __name__=="__main__":
    main()
