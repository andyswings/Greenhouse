import smbus2
import bme280
# TODO import relay modules

port1 = 1
address1 = 0x76
bus1 = smbus2.SMBus(port)
port2 = 1
address2 = 0x76
bus2 = smbus2.SMBus(port)

calibration_params1 = bme280.load_calibration_params(bus1, address1)
calibration_params2 = bme280.load_calibration_params(bus2, address2)

# compensated_reading object
data1 = bme280.sample(bus1, address1, calibration_params1)
data2 = bme280.sample(bus2, address2, calibration_params2)

# TODO Define pins for relays
# Heating, cooling and lighting controls
Exhaustfans_set1 = 2 # TODO set up pin num properly
Exhaustfans_set2 = 2 # TODO set up pin num properly
Vents = 2 # TODO set up pin num properly
Heaters = 2 # TODO set up pin num properly
Cooler_wall = 2 # TODO set up pin num properly
Grow_lights1 = 2 # TODO set up pin num properly
Grow_lights2 = 2 # TODO set up pin num properly

# Define pins for sensors
temp_sense1 = 2
temp_sense2 = 2
moisture_sensor1 = 2
moisture_sensor2 = 2
light_sensor = 2

# the compensated_reading class has the following attributes
# print(data.id)
# print(data.timestamp)
# print(data.temperature)
# print(data.pressure)
# print(data.humidity)

# there is a handy string representation too
# print(data)

temperature1 = data1.temperature
temperature2 = data2.temperature
humid1 = data1.humidity
humid2 = data2.humidity


def temp_control():
    if temperature1 or temperature2 >= 80:
        Exhaustfans_set1 = 1
    elif temperature1 or temperature2 >= 85:
        Exhaustfans_set1 = 1
        Exhaustfans_set2 = 1
    elif temperature1 or temperature2 >= 90:
        Exhaustfans_set1 = 1
        Exhaustfans_set2 = 1
        Cooler_wall = 1
    elif temperature1 or temperature2 <= 80:
        Exhaustfans_set1 = 0
        Exhaustfans_set2 = 0
    elif temperature1 or temperature2 <= 40:
        Exhaustfans_set1 = 0
        Exhaustfans_set2 = 0
        Cooler_wall = 0
        Vents = 0
        Heaters = 1

def humid_control():
    if humid1 or humid2 >= 60:
        Exhaustfans_set1 = 1
    elif humid1 or humid2 >= 70:
        Exhaustfans_set1 = 1
        Exhaustfans_set2 = 1
    elif humid1 or humid2 <= 50:
        Exhaustfans_set1 = 0
        Exhaustfans_set2 = 0
