#!/usr/bin/python3

import smbus
import time
import bme280 as bme
import RPi.GPIO as GPIO

DEVICE = 0x76 # Default device I2C address used for all three temperature sensors
bus1 = smbus.SMBus(1) # Rev 2 Pi, Pi 2 & Pi 3 uses bus 1
bus3 = smbus.SMBus(3) # Rev 1 Pi uses bus 0
bus4 = smbus.SMBus(4)

GPIO.setmode(GPIO.BCM) # Turn on the GPIO board
GPIO.setwarnings(False)

light_1 = 12

# Define heating, cooling and lighting control pins so that the Pi knows which pins to use
relay1 = 14
relay2 = 17
relay3 = 15
relay4 = 27
relay5 = 18
relay6 = 22
relay7 = 23
relay8 = 10

relay9 = 24
relay10 = 9
relay11 = 25
relay12 = 11
relay13 = 8
relay14 = 5
relay15 = 7
relay16 = 16

# Set Heating, cooling, and lighting pins as outputs
# Also pins are initially set to HIGH which is off since these are relays
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)
GPIO.setup(relay5, GPIO.OUT)
GPIO.setup(relay6, GPIO.OUT)
GPIO.setup(relay7, GPIO.OUT)
GPIO.setup(relay8, GPIO.OUT)
GPIO.setup(relay9, GPIO.OUT)
GPIO.setup(relay10, GPIO.OUT)
GPIO.setup(relay11, GPIO.OUT)
GPIO.setup(relay12, GPIO.OUT)
GPIO.setup(relay13, GPIO.OUT)
GPIO.setup(relay14, GPIO.OUT)
GPIO.setup(relay15, GPIO.OUT)
GPIO.setup(relay16, GPIO.OUT)
GPIO.setup(light_1, GPIO.IN)

def Day():
    if GPIO.input(light_1) == 1: # Night
        return 1
    else:
        return 0 # Day

def onrelay1():
    GPIO.output(relay1, GPIO.LOW)

def offrelay1():
    GPIO.output(relay1, GPIO.HIGH)

def onrelay2():
    GPIO.output(relay2, GPIO.LOW)

def offrelay2():
    GPIO.output(relay2, GPIO.HIGH)

def onrelay3():
    GPIO.output(relay3, GPIO.LOW)

def offrelay3():
    GPIO.output(relay3, GPIO.HIGH)

def onrelay4():
    GPIO.output(relay4, GPIO.LOW)

def offrelay4():
    GPIO.output(relay4, GPIO.HIGH)

def onrelay5():
    GPIO.output(relay5, GPIO.LOW)

def offrelay5():
    GPIO.output(relay5, GPIO.HIGH)

def onrelay6():
    GPIO.output(relay6, GPIO.LOW)

def offrelay6():
    GPIO.output(relay6, GPIO.HIGH)

def onrelay7():
    GPIO.output(relay7, GPIO.LOW)

def offrelay7():
    GPIO.output(relay7, GPIO.HIGH)

def onrelay8():
    GPIO.output(relay8, GPIO.LOW)

def offrelay8():
    GPIO.output(relay8, GPIO.HIGH)

def onrelay9():
    GPIO.output(relay9, GPIO.LOW)

def offrelay9():
    GPIO.output(relay9, GPIO.HIGH)

def onrelay10():
    GPIO.output(relay10, GPIO.LOW)

def offrelay10():
    GPIO.output(relay10, GPIO.HIGH)

def onrelay11():
    GPIO.output(relay11, GPIO.LOW)

def offrelay11():
    GPIO.output(relay11, GPIO.HIGH)

def onrelay12():
    GPIO.output(relay12, GPIO.LOW)

def offrelay12():
    GPIO.output(relay12, GPIO.HIGH)

def onrelay13():
    GPIO.output(relay13, GPIO.LOW)

def offrelay13():
    GPIO.output(relay13, GPIO.HIGH)

def onrelay14():
    GPIO.output(relay14, GPIO.LOW)

def offrelay14():
    GPIO.output(relay14, GPIO.HIGH)

def onrelay15():
    GPIO.output(relay15, GPIO.LOW)

def offrelay15():
    GPIO.output(relay15, GPIO.HIGH)

def onrelay16():
    GPIO.output(relay16, GPIO.LOW)

def offrelay16():
    GPIO.output(relay16, GPIO.HIGH)

def InsideTemp():
    in_temp = round(bme.av_temp(bus3, bus4),2)
    return in_temp

def OutsideTemp():
    out_temp = round(bme.temp(bus1),2)
    return out_temp

def InsideHumidity():
    in_humid = round(bme.av_humid(bus3, bus4))
    return in_humid

def OutsideHumidity():
    out_humid = round(bme.humid(bus1))
    return out_humid

def AtmosphericPressure():
    press = round(bme.pres(bus1))
    return press
