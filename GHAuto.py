#!/usr/bin/python3

import time
import GHmain
import json
import os

def CoolWaterON():
    GHmain.onrelay1()
def CoolWaterOFF():
    GHmain.offrelay1()
def Extra1ON():
    GHmain.onrelay2()
def Extra1OFF():
    GHmain.offrelay2()
def Extra2ON():
    GHmain.onrelay3()
def Extra2OFF():
    GHmain.offrelay3()
def Extra3ON():
    GHmain.onrelay4()
def Extra3OFF():
    GHmain.offrelay4()
def Fans1ON():
    GHmain.onrelay5()
def Fans1Off():
    GHmain.offrelay5()
def Fans2ON():
    GHmain.onrelay6()
def Fans2OFF():
    GHmain.offrelay6()
def UpFansON():
    GHmain.onrelay7()
def UpFansOFF():
    GHmain.offrelay7()
def VentsOPEN():
    GHmain.onrelay8()
def VentsCLOSED():
    GHmain.offrelay8()
def HeatON():
    GHmain.onrelay9()
def HeatOFF():
    GHmain.offrelay9()
def DehumidON():
    GHmain.onrelay10()
def DehumidOFF():
    GHmain.offrelay10()
def Lights1ON():
    GHmain.onrelay11()
def Lights1OFF():
    GHmain.offrelay11()
def Lights2ON():
    GHmain.onrelay12()
def Lights2OFF():
    GHmain.offrelay12()
def Drip1ON():
    GHmain.onrelay13()
def Drip1OFF():
    GHmain.offrelay13()
def Drip2ON():
    GHmain.onrelay14()
def Drip2OFF():
    GHmain.offrelay14()
def Drip3ON():
    GHmain.onrelay15()
def Drip3OFF():
    GHmain.offrelay15()
def Drip4ON():
    GHmain.onrelay16()
def Drip4OFF():
    GHmain.offrelay16()

def Dehumidify():
    if in_temp > (int(min_temp) + 15):
        # on(cooler_wall)
        Fans1ON()
        Fans2ON()
        DehumidOFF()
    else:
        # off(cooler_wall)
        Fans1OFF()
        Fans2OFF()
        DehumidON()

def HourNow():
    hour = time.strftime("%H", time.localtime())
    return int(hour)

# This is where all the temperature control happens
def Auto():
    with open("GHsettings.json") as f:
        data = json.load(f)
    automanual = data["automan"]

    while automanual == 1: # This will later be set to 'While True' when testing is done
        with open("GHsettings.json") as f:
            data = json.load(f)
        automanual = data["automan"]
        max_temp = data["maxtemp"]
        min_temp = data["mintemp"]
        max_humid = data["maxhumid"]
        day_hours = data["dayhours"]
        day_begin = data["daybegin"]

        high_off_temp = int(max_temp) - 5
        low_off_temp = int(min_temp) + 5

        out_temp = GHmain.OutsideTemp()
        out_humid = GHmain.OutsideHumidity()
        in_temp = GHmain.InsideTemp()
        in_humid = GHmain.InsideHumidity()
        #
        if GHmain.Day() == 1: # This code runs if it is night
            if HourNow() >= int(day_begin):
                print("It is night.")
                Lights1ON()
                Lights2ON()
            elif HourNow() < (int(day_begin) + int(day_hours)):
                Lights1ON()
                Lights2ON()
            else:
                Lights1OFF()
                Lights2OFF()
            #
            # This code only runs if the outside temperature is less than the inside temperature
            #
            if out_temp < in_temp: # Determine if outside temperature is less than inside temperature
                print("Outside temperature is lower than inside temperature")
                if in_temp >= max_temp:
                    if in_temp > high_off_temp:
                        # on(cooler_wall) # TODO: create the ability to open or close partially
                        Fans1ON()
                        Fans2ON()
                    else:
                        Fans1OFF()
                        Fans2OFF()
                elif in_temp <= min_temp:
                    if in_temp < low_off_temp:
                        # off(cooler_wall) # TODO: create the ability to open or close partially
                        HeatON()
                    else:
                        HeatOFF()
            # This code only runs if the outside temperature is greater than the inside temperature
            elif out_temp <= in_temp:
                print("Outside temperature is higher than inside temperature")
                if in_temp >= max_temp:
                    if in_temp > high_off_temp:
                        # on(cooler_wall) # TODO: create the ability to open or close partially
                        Fans1ON()
                        Fans2ON()
                    else:
                        # on(cooler_wall)
                        Fans1OFF()
                        Fans2OFF()
                elif in_temp <= min_temp:
                    if in_temp < low_off_temp:
                        # off(cooler_wall) # TODO: create the ability to open or close partially
                        HeatON()
                    else:
                        HeatOFF()
            elif in_humid > max_humid:
                Dehumidify()
        #
        elif GPIO.input(light_1) == 0: # This code runs if it is day
            print("It is day.")
            Lights1OFF()
            Lights2OFF()
            #
            # This code only runs if the outside temperature is less than the inside temperature
            #
            if out_temp < in_temp: # Determine if outside temperature is less than inside temperature
                print("Outside temperature is lower than inside temperature")
                if in_temp >= max_temp:
                    if in_temp > high_off_temp:
                        # on(cooler_wall) # TODO: create the ability to open or close partially
                        Fans1ON()
                        Fans2ON()
                    else:
                        # on(cooler_wall) # TODO: create the ability to open or close partially
                        Fans1OFF()
                        Fans2OFF()
                elif in_temp <= min_temp:
                    if in_temp < low_off_temp:
                        # off(cooler_wall) # TODO: create the ability to open or close partially
                        HeatON()
                    else:
                        # off(cooler_wall) # TODO: create the ability to open or close partially
                        HeatOFF()
            #
            # This code only runs if the outside temperature is greater than the inside temperature
            elif out_temp >= in_temp:
                print("Outside temperature is higher than inside temperature")
                if in_temp >= max_temp:
                    if in_temp > high_off_temp:
                        # on(cooler_wall) # TODO: create the ability to open or close partially
                        Fans1ON()
                        Fans2ON()
                    else:
                        # on(cooler_wall) # TODO: create the ability to open or close partially
                        Fans1OFF()
                        Fans2OFF()
                elif in_temp <= min_temp:
                    if in_temp < low_off_temp:
                        # off(cooler_wall) # TODO: create the ability to open or close partially
                        HeatON()
                    else:
                        # off(cooler_wall) # TODO: create the ability to open or close partially
                        HeatOFF()
            elif in_humid > max_humid:
                Dehumidify()
        time.sleep(0.5)
        x = x - 1
