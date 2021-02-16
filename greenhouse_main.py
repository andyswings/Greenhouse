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

# Define temperature levels for use in controlling the greenhouse
absolute_max_temp = 32.5
yellow_high_temp = 29.5
safe_high_temp = 26.7
safe_low_temp = 21.0
yellow_low_temp = 18.5
absolute_min_temp = 15.5

# Define humidity levels for use in controlling the greenhouse
max_humid = 60
yellow_humid = 55
ok_humid = 50

moist_1 = 4
light_1 = 12

# Define heating, cooling and lighting control pins so that the Pi knows which pins to use
exhaustfans_set1 = 14
exhaustfans_set2 = 15
vents = 18
heaters = 23
cooler_wall = 24
cooler_water = 25
grow_lights1 = 8
grow_lights2 = 7

# Set Heating, cooling, and lighting pins as outputs
# Also pins are initially set to HIGH which is off since these are relays
GPIO.setup(exhaustfans_set1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(exhaustfans_set2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(vents, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(heaters, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(cooler_wall, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(cooler_water, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(grow_lights1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(grow_lights2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(moist_1, GPIO.IN)
GPIO.setup(light_1, GPIO.IN)

def on(relay): # Function to turn on relays
    GPIO.output(relay, GPIO.LOW)

def off(relay): # Function to turn off relays
    GPIO.output(relay, GPIO.HIGH)

# This is where all the temperature control happens
def temp_control():
    x = 10
    while x > 0: # This will later be set to 'While True' when testing is done
        out_temp = bme.temp(bus1)
        out_humid = bme.humid(bus1)
        in_temp = bme.av_temp(bus3, bus4)
        in_humid = bme.av_humid(bus3, bus4)
        #
        if GPIO.input(light_1) == 1: # This code runs if it is night
            print("It is night.")
            on(grow_lights1)
            on(grow_lights2)
            #
            # This code only runs if the outside temperature is less than the inside temperature
            if out_temp < in_temp: # Determine if outside temperature is less than inside temperature
                print("Outside temperature is lower than inside temperature")
                if in_temp >= absolute_max_temp or in_humid >= max_humid:
                    on(cooler_wall) # TODO: create the ability to open or close partially
                    on(exhaustfans_set1)
                    on(exhaustfans_set2)
                elif in_temp >= yellow_high_temp or in_humid >= yellow_humid:
                    on(cooler_wall) # TODO: create the ability to open or close partially
                    on(exhaustfans_set1)
                    off(exhaustfans_set2)
                elif in_temp < safe_high_temp and in_temp > safe_low_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    off(exhaustfans_set1)
                    off(exhaustfans_set2)
                elif in_temp < yellow_low_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    on(heaters)
                elif in_temp <= absolute_min_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    on(heaters)
            #
            # This code only runs if the outside temperature is greater than the inside temperature
            else:
                print("Outside temperature is higher than inside temperature")
                if in_temp >= absolute_max_temp or in_humid >= max_humid:
                    on(cooler_wall) # TODO: create the ability to open or close partially
                    on(exhaustfans_set1)
                    on(exhaustfans_set2)
                elif in_temp >= yellow_high_temp or in_humid >= yellow_humid:
                    on(cooler_wall) # TODO: create the ability to open or close partially
                    on(exhaustfans_set1)
                    off(exhaustfans_set2)
                elif in_temp < safe_high_temp and in_temp > safe_low_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    off(exhaustfans_set1)
                    off(exhaustfans_set2)
                elif in_temp < yellow_low_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    on(heaters)
                elif in_temp <= absolute_min_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    on(heaters)
        #
        elif GPIO.input(light_1) == 0: # This code runs if it is day
            print("It is day.")
            off(grow_lights1)
            off(grow_lights2)
            #
            # This code only runs if the outside temperature is less than the inside temperature
            if out_temp < in_temp: # Determine if outside temperature is less than inside temperature
                print("Outside temperature is lower than inside temperature")
                if in_temp >= absolute_max_temp or in_humid >= max_humid:
                    on(cooler_wall) # TODO: create the ability to open or close partially
                    on(exhaustfans_set1)
                    on(exhaustfans_set2)
                elif in_temp >= yellow_high_temp or in_humid >= yellow_humid:
                    on(cooler_wall) # TODO: create the ability to open or close partially
                    on(exhaustfans_set1)
                    off(exhaustfans_set2)
                elif in_temp < safe_high_temp and in_temp > safe_low_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    off(exhaustfans_set1)
                    off(exhaustfans_set2)
                elif in_temp < yellow_low_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    on(heaters)
                elif in_temp <= absolute_min_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    on(heaters)
            #
            # This code only runs if the outside temperature is greater than the inside temperature
            else:
                print("Outside temperature is higher than inside temperature")
                if in_temp >= absolute_max_temp or in_humid >= max_humid:
                    on(cooler_wall) # TODO: create the ability to open or close partially
                    on(exhaustfans_set1)
                    on(exhaustfans_set2)
                elif in_temp >= yellow_high_temp or in_humid >= yellow_humid:
                    on(cooler_wall) # TODO: create the ability to open or close partially
                    on(exhaustfans_set1)
                    off(exhaustfans_set2)
                elif in_temp < safe_high_temp and in_temp > safe_low_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    off(exhaustfans_set1)
                    off(exhaustfans_set2)
                elif in_temp < yellow_low_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    on(heaters)
                elif in_temp <= absolute_min_temp:
                    off(cooler_wall) # TODO: create the ability to open or close partially
                    on(heaters)
        time.sleep(0.5)
        x = x - 1

def all_on(): # Turns on all relays
    GPIO.output(exhaustfans_set1, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(exhaustfans_set2, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(vents, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(heaters, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(cooler_wall, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(cooler_water, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(grow_lights2, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(grow_lights1, GPIO.LOW)
    time.sleep(0.1)
    print("All relays on")

def all_off(): # Turns off all relays
    GPIO.output(exhaustfans_set1, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(exhaustfans_set2, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(vents, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(heaters, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(cooler_wall, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(cooler_water, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(grow_lights2, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(grow_lights1, GPIO.HIGH)
    print("All relays off")
    print(" ")

def sense_test(): # The only purpose of this function is to test sensors
    print("'Outside' sensor")
    print("# Temperature: ", bme.temp(bus1), "C")
    print("# Pressure: ", round(bme.pres(bus1), 2), "hPa")
    print("# Humidity: ", round(bme.humid(bus1), 2), "%")
    print("# Calculated altitude: ", bme.alt(bus1), "ft")
    print(" ")
    print("'Inside' sensor 1")
    print("# Temperature: ", bme.temp(bus3), "C")
    print("# Pressure: ", round(bme.pres(bus3), 2), "hPa")
    print("# Humidity: ", round(bme.humid(bus3), 2), "%")
    print("# Calculated altitude: ", bme.alt(bus3), "ft")
    print(" ")
    print("'Inside' sensor 2")
    print("# Temperature: ", bme.temp(bus4), "C")
    print("# Pressure: ", round(bme.pres(bus4), 2), "hPa")
    print("# Humidity: ", round(bme.humid(bus4), 2), "%")
    print("# Calculated altitude: ", bme.alt(bus4), "ft")
    print(" ")
    if GPIO.input(moist_1) == 1:
        print("I'm thirsty! Give me water!") # TRUE == no water, FALSE == enough water sensitivity adjusted on sensor
    else:
        print("I have enough water.")
    if GPIO.input(light_1) == 0:
        print("It is day.")
    else:
        print("It is night.")
    print(" ")

def relay_test(): # The only purpose of this function is to test relays
    all_on()
    all_off()

# This is the main program
def main():
    try:
        sense_test()
        relay_test()
        temp_control()
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__=="__main__":
    main()
