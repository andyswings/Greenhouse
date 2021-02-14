#!/usr/bin/python

import smbus
import time
from ctypes import c_short
from ctypes import c_byte
from ctypes import c_ubyte
import RPi.GPIO as GPIO

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

DEVICE = 0x76 # Default device I2C address used for all three temperature sensors
bus1 = smbus.SMBus(1) # Rev 2 Pi, Pi 2 & Pi 3 uses bus 1
bus3 = smbus.SMBus(3) # Rev 1 Pi uses bus 0
bus4 = smbus.SMBus(4)

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

def getShort(data, index):
    # return two bytes from data as a signed 16-bit value
    return c_short((data[index+1] << 8) + data[index]).value

def getUShort(data, index):
    # return two bytes from data as an unsigned 16-bit value
    return (data[index+1] << 8) + data[index]

def getChar(data,index):
    # return one byte from data as a signed char
    result = data[index]
    if result > 127:
        result -= 256
    return result

def getUChar(data,index):
    # return one byte from data as an unsigned char
    result =  data[index] & 0xFF
    return result

def readBME280All(addr, bus):
    # Register Addresses
    REG_DATA = 0xF7
    REG_CONTROL = 0xF4
    REG_CONFIG  = 0xF5

    REG_CONTROL_HUM = 0xF2
    REG_HUM_MSB = 0xFD
    REG_HUM_LSB = 0xFE

    # Oversample setting - page 27
    OVERSAMPLE_TEMP = 2
    OVERSAMPLE_PRES = 2
    MODE = 1

    # Oversample setting for humidity register - page 26
    OVERSAMPLE_HUM = 2
    bus.write_byte_data(addr, REG_CONTROL_HUM, OVERSAMPLE_HUM)

    control = OVERSAMPLE_TEMP<<5 | OVERSAMPLE_PRES<<2 | MODE
    bus.write_byte_data(addr, REG_CONTROL, control)

    # Read blocks of calibration data from EEPROM
    # See Page 22 data sheet
    cal1 = bus.read_i2c_block_data(addr, 0x88, 24)
    cal2 = bus.read_i2c_block_data(addr, 0xA1, 1)
    cal3 = bus.read_i2c_block_data(addr, 0xE1, 7)

    # Convert byte data to word values
    dig_T1 = getUShort(cal1, 0)
    dig_T2 = getShort(cal1, 2)
    dig_T3 = getShort(cal1, 4)

    dig_P1 = getUShort(cal1, 6)
    dig_P2 = getShort(cal1, 8)
    dig_P3 = getShort(cal1, 10)
    dig_P4 = getShort(cal1, 12)
    dig_P5 = getShort(cal1, 14)
    dig_P6 = getShort(cal1, 16)
    dig_P7 = getShort(cal1, 18)
    dig_P8 = getShort(cal1, 20)
    dig_P9 = getShort(cal1, 22)

    dig_H1 = getUChar(cal2, 0)
    dig_H2 = getShort(cal3, 0)
    dig_H3 = getUChar(cal3, 2)

    dig_H4 = getChar(cal3, 3)
    dig_H4 = (dig_H4 << 24) >> 20
    dig_H4 = dig_H4 | (getChar(cal3, 4) & 0x0F)

    dig_H5 = getChar(cal3, 5)
    dig_H5 = (dig_H5 << 24) >> 20
    dig_H5 = dig_H5 | (getUChar(cal3, 4) >> 4 & 0x0F)

    dig_H6 = getChar(cal3, 6)

    # Wait in ms (Datasheet Appendix B: Measurement time and current calculation)
    wait_time = 1.25 + (2.3 * OVERSAMPLE_TEMP) + ((2.3 * OVERSAMPLE_PRES) + 0.575) + ((2.3 * OVERSAMPLE_HUM)+0.575)
    time.sleep(wait_time/1000)  # Wait the required time

    # Read temperature/pressure/humidity
    data = bus.read_i2c_block_data(addr, REG_DATA, 8)
    pres_raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
    temp_raw = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
    hum_raw = (data[6] << 8) | data[7]

    #Refine temperature
    var1 = ((((temp_raw>>3)-(dig_T1<<1)))*(dig_T2)) >> 11
    var2 = (((((temp_raw>>4) - (dig_T1)) * ((temp_raw>>4) - (dig_T1))) >> 12) * (dig_T3)) >> 14
    t_fine = var1+var2
    temperature = float(((t_fine * 5) + 128) >> 8);

    # Refine pressure and adjust for temperature
    var1 = t_fine / 2.0 - 64000.0
    var2 = var1 * var1 * dig_P6 / 32768.0
    var2 = var2 + var1 * dig_P5 * 2.0
    var2 = var2 / 4.0 + dig_P4 * 65536.0
    var1 = (dig_P3 * var1 * var1 / 524288.0 + dig_P2 * var1) / 524288.0
    var1 = (1.0 + var1 / 32768.0) * dig_P1
    if var1 == 0:
        pressure=0
    else:
        pressure = 1048576.0 - pres_raw
        pressure = ((pressure - var2 / 4096.0) * 6250.0) / var1
        var1 = dig_P9 * pressure * pressure / 2147483648.0
        var2 = pressure * dig_P8 / 32768.0
        pressure = pressure + (var1 + var2 + dig_P7) / 16.0

    # Refine humidity
    humidity = t_fine - 76800.0
    humidity = (hum_raw - (dig_H4 * 64.0 + dig_H5 / 16384.0 * humidity)) * (dig_H2 / 65536.0 * (1.0 + dig_H6 / 67108864.0 * humidity * (1.0 + dig_H3 / 67108864.0 * humidity)))
    humidity = humidity * (1.0 - dig_H1 * humidity / 524288.0)
    if humidity > 100:
        humidity = 100
    elif humidity < 0:
        humidity = 0

    return temperature/100.0,pressure/100.0,humidity

def alt(bus): # Function to calculate altitude
    temperature,pressure,humidity = readBME280All(DEVICE, bus)
    std_pres = 1013.25
    alt_var = float(std_pres / pressure) ** 0.19022256 - 1
    altitude = round((float(temperature + 273.15) * alt_var) / 0.0065 * 3.2808399, 1)
    return altitude

def temp(bus): # Function to return temperature separately from other data
    temperature,pressure,humidity = readBME280All(DEVICE, bus)
    return temperature

def av_temp(bus_x, bus_y): # Function to return average temperature
    ave_temp = float(temp(bus_x) + temp(bus_y)) / 2.0
    return ave_temp

def pres(bus): # Function to return pressure separately from other data
    temperature,pressure,humidity = readBME280All(DEVICE, bus)
    return pressure

def humid(bus): # Function to return humidity separately from other data
    temperature,pressure,humidity = readBME280All(DEVICE, bus)
    return humidity

def av_humid(bus_x, bus_y): # Function to return average humidity
    ave_humid = float(humid(bus_x) + humid(bus_y)) / 2.0
    return ave_humid

def on(relay): # Function to turn on relays
    GPIO.output(relay, GPIO.LOW)

def off(relay): # Function to turn off relays
    GPIO.output(relay, GPIO.HIGH)

# This is where all the temperature control happens
def temp_control():
    x = 10
    while x > 0: # This will later be set to 'While True' when testing is done
        out_temp = temp(bus1)
        out_humid = humid(bus1)
        in_temp = av_temp(bus3, bus4)
        in_humid = av_humid(bus3, bus4)
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
    time.sleep(0.4)
    GPIO.output(exhaustfans_set2, GPIO.LOW)
    time.sleep(0.4)
    GPIO.output(vents, GPIO.LOW)
    time.sleep(0.4)
    GPIO.output(heaters, GPIO.LOW)
    time.sleep(0.4)
    GPIO.output(cooler_wall, GPIO.LOW)
    time.sleep(0.4)
    GPIO.output(cooler_water, GPIO.LOW)
    time.sleep(0.4)
    GPIO.output(grow_lights2, GPIO.LOW)
    time.sleep(0.4)
    GPIO.output(grow_lights1, GPIO.LOW)
    time.sleep(0.4)

def all_off(): # Turns off all relays
    GPIO.output(exhaustfans_set1, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(exhaustfans_set2, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(vents, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(heaters, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(cooler_wall, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(cooler_water, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(grow_lights2, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(grow_lights1, GPIO.HIGH)

def sense_test(): # The only purpose of this function is to test sensors
    print("'Outside' sensor")
    print("# Temperature: ", temp(bus1), "C")
    print("# Pressure: ", round(pres(bus1), 2), "hPa")
    print("# Humidity: ", round(humid(bus1), 2), "%")
    print("# Calculated altitude: ", alt(bus1), "ft")
    print(" ")
    print("'Inside' sensor 1")
    print("# Temperature: ", temp(bus3), "C")
    print("# Pressure: ", round(pres(bus3), 2), "hPa")
    print("# Humidity: ", round(humid(bus3), 2), "%")
    print("# Calculated altitude: ", alt(bus3), "ft")
    print(" ")
    print("'Inside' sensor 2")
    print("# Temperature: ", temp(bus4), "C")
    print("# Pressure: ", round(pres(bus4), 2), "hPa")
    print("# Humidity: ", round(humid(bus4), 2), "%")
    print("# Calculated altitude: ", alt(bus4), "ft")
    print(" ")
    print(GPIO.input(moist_1)) # TRUE == no water, FALSE == enough water sensitivity adjusted on sensor
    print(GPIO.input(light_1)) # TRUE == dark, FALSE == light sensitivity adjusted on sensor
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
