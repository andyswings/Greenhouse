#!/usr/bin/python

import smbus
import time
from ctypes import c_short
from ctypes import c_byte
from ctypes import c_ubyte
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # Turn on the GPIO board
GPIO.setwarnings(False)

DEVICE = 0x76 # Default device I2C address

bus1 = smbus.SMBus(1) # Rev 2 Pi, Pi 2 & Pi 3 uses bus 1
                     # Rev 1 Pi uses bus 0
bus4 = smbus.SMBus(4)

# Define heating, cooling and lighting control pins
Exhaustfans_set1 = 14
Exhaustfans_set2 = 15
Vents = 18
Heaters = 23
Cooler_wall = 24
Grow_lights1 = 25
Grow_lights2 = 8
Extra = 7 # This is an extra relay and can be used for anything

# Set Heating, cooling, and lighting pins as outputs
# Also pins are initially set to HIGH which is off since these are relays
GPIO.setup(Exhaustfans_set1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Exhaustfans_set2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Vents, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Heaters, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Cooler_wall, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Grow_lights1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Grow_lights2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(Extra, GPIO.OUT, initial=GPIO.HIGH) # Extra relay is turned off.

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

def readBME280ID(addr, bus):
    # Chip ID Register Address
    REG_ID     = 0xD0
    (chip_id, chip_version) = bus.read_i2c_block_data(addr, REG_ID, 2)
    return (chip_id, chip_version)

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

def alt(bus):
    temperature,pressure,humidity = readBME280All(DEVICE, bus)
    std_pres = 1013.25
    alt_var = float(std_pres / pressure) ** 0.19022256 - 1
    altitude = round((float(temperature + 273.15) * alt_var) / 0.0065 * 3.2808399, 1)
    print("# Calculated altitude: ", altitude, "ft")
    return altitude

def temp(bus):
    temperature,pressure,humidity = readBME280All(DEVICE, bus)
    print("# Temperature: ", temperature, "C")
    return temperature

def pres(bus):
    temperature,pressure,humidity = readBME280All(DEVICE, bus)
    print("# Pressure: ", round(pressure, 2), "hPa")
    return pressure

def humid(bus):
    temperature,pressure,humidity = readBME280All(DEVICE, bus)
    print("# Humidity: ", round(humidity, 2), "%")
    return humidity

def sensor_id(bus):
    (chip_id, chip_version) = readBME280ID(DEVICE, bus)
    print ("Chip ID     :", chip_id)
    print ("Version     :", chip_version)

def all_on():
    GPIO.output(Exhaustfans_set1, GPIO.LOW)
    time.sleep(1)
    GPIO.output(Exhaustfans_set2, GPIO.LOW)
    time.sleep(1)
    GPIO.output(Vents, GPIO.LOW)
    time.sleep(1)
    GPIO.output(Heaters, GPIO.LOW)
    time.sleep(1)
    GPIO.output(Cooler_wall, GPIO.LOW)
    time.sleep(1)
    GPIO.output(Grow_lights1, GPIO.LOW)
    time.sleep(1)
    GPIO.output(Grow_lights2, GPIO.LOW)
    time.sleep(1)
    GPIO.output(Extra, GPIO.LOW)
    time.sleep(1)

def all_off():
    GPIO.output(Exhaustfans_set1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(Exhaustfans_set2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(Vents, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(Heaters, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(Cooler_wall, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(Grow_lights1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(Grow_lights2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(Extra, GPIO.HIGH)

def main():
    try:
        print("Sensor 1")
        temp(bus1)
        pres(bus1)
        humid(bus1)
        alt(bus1)

        print(" ")
        print("Sensor 2")
        temp(bus4)
        pres(bus4)
        humid(bus4)
        alt(bus4)
        
        all_on()
        all_off()
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__=="__main__":
    main()
