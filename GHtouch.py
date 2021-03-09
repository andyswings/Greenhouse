#!/usr/bin/python3

import json
import os
import GHmain as gh
import hd38
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        MainWindow.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/andrew/Code/Repositories/Greenhouse/GHicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #
        ####### Relay01 #######
        #
        self.Relay01 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay01.setGeometry(QtCore.QRect(130, 190, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay01.setFont(font)
        self.Relay01.setObjectName("Relay01")
        self.Relay01.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay1"]
        if currentvalue == "1":
            self.Relay01.setChecked(True)
            self.Relay01.setText("Cool H2O ON")
        else:
            self.Relay01.setChecked(False)
            self.Relay01.setText("Cool H2O OFF")
        #
        ####### Relay02 #######
        #
        self.Relay02 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay02.setGeometry(QtCore.QRect(130, 260, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay02.setFont(font)
        self.Relay02.setObjectName("Relay02")
        self.Relay02.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay2"]
        if currentvalue == "1":
            self.Relay02.setChecked(True)
            self.Relay02.setText("Extra 1 ON")
        else:
            self.Relay02.setChecked(False)
            self.Relay02.setText("Extra 1 OFF")
        #
        ####### Relay03 #######
        #
        self.Relay03 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay03.setGeometry(QtCore.QRect(130, 330, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay03.setFont(font)
        self.Relay03.setObjectName("Relay03")
        self.Relay03.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay3"]
        if currentvalue == "1":
            self.Relay03.setChecked(True)
            self.Relay03.setText("Extra 2 ON")
        else:
            self.Relay03.setChecked(False)
            self.Relay03.setText("Extra 2 OFF")
        #
        ####### Relay04 #######
        #
        self.Relay04 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay04.setGeometry(QtCore.QRect(130, 400, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay04.setFont(font)
        self.Relay04.setObjectName("Relay04")
        self.Relay04.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay4"]
        if currentvalue == "1":
            self.Relay04.setChecked(True)
            self.Relay04.setText("Extra 3 ON")
        else:
            self.Relay04.setChecked(False)
            self.Relay04.setText("Extra 3 OFF")
        #
        ####### Relay05 #######
        #
        self.Relay05 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay05.setGeometry(QtCore.QRect(260, 190, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay05.setFont(font)
        self.Relay05.setObjectName("Relay05")
        self.Relay05.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay5"]
        if currentvalue == "1":
            self.Relay05.setChecked(True)
            self.Relay05.setText("Fans 1 ON")
        else:
            self.Relay05.setChecked(False)
            self.Relay05.setText("Fans 1 OFF")
        #
        ####### Relay06 #######
        #
        self.Relay06 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay06.setGeometry(QtCore.QRect(260, 260, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay06.setFont(font)
        self.Relay06.setObjectName("Relay06")
        self.Relay06.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay6"]
        if currentvalue == "1":
            self.Relay06.setChecked(True)
            self.Relay06.setText("Fans 2 ON")
        else:
            self.Relay06.setChecked(False)
            self.Relay06.setText("Fans 2 OFF")
        #
        ####### Relay07 #######
        #
        self.Relay07 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay07.setGeometry(QtCore.QRect(260, 330, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay07.setFont(font)
        self.Relay07.setObjectName("Relay07")
        self.Relay07.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay7"]
        if currentvalue == "1":
            self.Relay07.setChecked(True)
            self.Relay07.setText("Up Fans ON")
        else:
            self.Relay07.setChecked(False)
            self.Relay07.setText("Up Fans OFF")
        #
        ####### Relay08 #######
        #
        self.Relay08 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay08.setGeometry(QtCore.QRect(260, 400, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay08.setFont(font)
        self.Relay08.setObjectName("Relay08")
        self.Relay08.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay8"]
        if currentvalue == "1":
            self.Relay08.setChecked(True)
            self.Relay08.setText("Vents ON")
        else:
            self.Relay08.setChecked(False)
            self.Relay08.setText("Vents OFF")
        #
        ####### Relay09 #######
        #
        self.Relay09 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay09.setGeometry(QtCore.QRect(390, 190, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay09.setFont(font)
        self.Relay09.setObjectName("Relay09")
        self.Relay09.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay9"]
        if currentvalue == "1":
            self.Relay09.setChecked(True)
            self.Relay09.setText("Heaters ON")
        else:
            self.Relay09.setChecked(False)
            self.Relay09.setText("Heaters OFF")
        #
        ####### Relay10 #######
        #
        self.Relay10 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay10.setGeometry(QtCore.QRect(390, 260, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay10.setFont(font)
        self.Relay10.setObjectName("Relay10")
        self.Relay10.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay10"]
        if currentvalue == "1":
            self.Relay10.setChecked(True)
            self.Relay10.setText("Dehumid ON")
        else:
            self.Relay10.setChecked(False)
            self.Relay10.setText("Dehumid OFF")
        #
        ####### Relay11 #######
        #
        self.Relay11 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay11.setGeometry(QtCore.QRect(390, 330, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay11.setFont(font)
        self.Relay11.setObjectName("Relay11")
        self.Relay11.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay11"]
        if currentvalue == "1":
            self.Relay11.setChecked(True)
            self.Relay11.setText("Lights 1 ON")
        else:
            self.Relay11.setChecked(False)
            self.Relay11.setText("Lights 1 OFF")
        #
        ####### Relay12 #######
        #
        self.Relay12 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay12.setGeometry(QtCore.QRect(390, 400, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay12.setFont(font)
        self.Relay12.setObjectName("Relay12")
        self.Relay12.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay12"]
        if currentvalue == "1":
            self.Relay12.setChecked(True)
            self.Relay12.setText("Lights 2 ON")
        else:
            self.Relay12.setChecked(False)
            self.Relay12.setText("Lights 2 OFF")
        #
        ####### Relay13 #######
        #
        self.Relay13 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay13.setGeometry(QtCore.QRect(520, 190, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay13.setFont(font)
        self.Relay13.setObjectName("Relay13")
        self.Relay13.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay13"]
        if currentvalue == "1":
            self.Relay13.setChecked(True)
            self.Relay13.setText("Drip 1 ON")
        else:
            self.Relay13.setChecked(False)
            self.Relay13.setText("Drip 1 OFF")
        #
        ####### Relay14 #######
        #
        self.Relay14 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay14.setGeometry(QtCore.QRect(520, 260, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay14.setFont(font)
        self.Relay14.setObjectName("Relay14")
        self.Relay14.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay14"]
        if currentvalue == "1":
            self.Relay14.setChecked(True)
            self.Relay14.setText("Drip 2 ON")
        else:
            self.Relay14.setChecked(False)
            self.Relay14.setText("Drip 2 OFF")
        #
        ####### Relay15 #######
        #
        self.Relay15 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay15.setGeometry(QtCore.QRect(520, 330, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay15.setFont(font)
        self.Relay15.setObjectName("Relay15")
        self.Relay15.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay15"]
        if currentvalue == "1":
            self.Relay15.setChecked(True)
            self.Relay15.setText("Drip 3 ON")
        else:
            self.Relay15.setChecked(False)
            self.Relay15.setText("Drip 3 OFF")
        #
        ####### Relay16 #######
        #
        self.Relay16 = QtWidgets.QPushButton(self.centralwidget)
        self.Relay16.setGeometry(QtCore.QRect(520, 400, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Relay16.setFont(font)
        self.Relay16.setObjectName("Relay16")
        self.Relay16.setCheckable(True)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["relay16"]
        if currentvalue == "1":
            self.Relay16.setChecked(True)
            self.Relay16.setText("Drip 4 ON")
        else:
            self.Relay16.setChecked(False)
            self.Relay16.setText("Drip 4 OFF")
        #
        ####### Slider #######
        #
        self.Slider = QtWidgets.QSlider(self.centralwidget)
        self.Slider.setGeometry(QtCore.QRect(29, 269, 21, 201))
        self.Slider.setOrientation(QtCore.Qt.Vertical)
        self.Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Slider.setMinimum(1)
        self.Slider.setMaximum(5)
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = int(settings["slider"])
        self.Slider.setValue(currentvalue)
        self.Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Slider.setTickInterval(1)
        self.Slider.setObjectName("Slider")
        #
        ####### Slider Set btn #######
        #
        self.SliderSet = QtWidgets.QPushButton(self.centralwidget)
        self.SliderSet.setGeometry(QtCore.QRect(80, 270, 41, 201))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SliderSet.setFont(font)
        self.SliderSet.setText("SET")
        self.SliderSet.setCheckable(False)
        self.SliderSet.setObjectName("SliderSet")
        #
        ####### MaxTemp set/display #######
        #
        self.MaxTempPlus = QtWidgets.QPushButton(self.centralwidget)
        self.MaxTempPlus.setGeometry(QtCore.QRect(750, 104, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MaxTempPlus.setFont(font)
        self.MaxTempPlus.setText("+")
        self.MaxTempPlus.setObjectName("MaxTempPlus")
        #
        self.MaxTempMinus = QtWidgets.QPushButton(self.centralwidget)
        self.MaxTempMinus.setGeometry(QtCore.QRect(660, 104, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.MaxTempMinus.setFont(font)
        self.MaxTempMinus.setText("-")
        self.MaxTempMinus.setObjectName("MaxTempMinus")
        #
        self.MaxTempDisp = QtWidgets.QLabel(self.centralwidget)
        self.MaxTempDisp.setGeometry(QtCore.QRect(700, 104, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MaxTempDisp.setFont(font)
        self.MaxTempDisp.setObjectName("MaxTempDisp")
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        maxtempvalue = " " + settings["maxtemp"]
        self.MaxTempDisp.setText(maxtempvalue)
        #
        ####### MinTemp set/display #######
        #
        self.MinTempDisp = QtWidgets.QLabel(self.centralwidget)
        self.MinTempDisp.setGeometry(QtCore.QRect(700, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MinTempDisp.setFont(font)
        self.MinTempDisp.setObjectName("MinTempDisp")
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        mintempvalue = " " + settings["mintemp"]
        self.MinTempDisp.setText(mintempvalue)
        #
        self.MinTempPlus = QtWidgets.QPushButton(self.centralwidget)
        self.MinTempPlus.setGeometry(QtCore.QRect(750, 180, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MinTempPlus.setFont(font)
        self.MinTempPlus.setText("+")
        self.MinTempPlus.setObjectName("MinTempPlus")
        #
        self.MinTempMinus = QtWidgets.QPushButton(self.centralwidget)
        self.MinTempMinus.setGeometry(QtCore.QRect(660, 180, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.MinTempMinus.setFont(font)
        self.MinTempMinus.setText("-")
        self.MinTempMinus.setObjectName("MinTempMinus")
        #
        ####### MaxHumid set/display #######
        #
        self.MaxHumidDisp = QtWidgets.QLabel(self.centralwidget)
        self.MaxHumidDisp.setGeometry(QtCore.QRect(700, 260, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MaxHumidDisp.setFont(font)
        self.MaxHumidDisp.setObjectName("MaxHumidDisp")
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        maxhumidvalue = " " + settings["maxhumid"]
        self.MaxHumidDisp.setText(maxhumidvalue)
        #
        self.MaxHumidPlus = QtWidgets.QPushButton(self.centralwidget)
        self.MaxHumidPlus.setGeometry(QtCore.QRect(750, 260, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MaxHumidPlus.setFont(font)
        self.MaxHumidPlus.setText("+")
        self.MaxHumidPlus.setObjectName("MaxHumidPlus")
        #
        self.MaxHumidMinus = QtWidgets.QPushButton(self.centralwidget)
        self.MaxHumidMinus.setGeometry(QtCore.QRect(660, 260, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.MaxHumidMinus.setFont(font)
        self.MaxHumidMinus.setText("-")
        self.MaxHumidMinus.setObjectName("MaxHumidMinus")
        #
        ####### DayHours set/display #######
        #
        self.DayHoursDisp = QtWidgets.QLabel(self.centralwidget)
        self.DayHoursDisp.setGeometry(QtCore.QRect(700, 340, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.DayHoursDisp.setFont(font)
        self.DayHoursDisp.setObjectName("DayHoursDisp")
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        dayhoursvalue = " " + settings["dayhours"]
        self.DayHoursDisp.setText(dayhoursvalue)
        #
        self.DayHoursPlus = QtWidgets.QPushButton(self.centralwidget)
        self.DayHoursPlus.setGeometry(QtCore.QRect(750, 340, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.DayHoursPlus.setFont(font)
        self.DayHoursPlus.setText("+")
        self.DayHoursPlus.setObjectName("DayHoursPlus")
        #
        self.DayHoursMinus = QtWidgets.QPushButton(self.centralwidget)
        self.DayHoursMinus.setGeometry(QtCore.QRect(660, 340, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.DayHoursMinus.setFont(font)
        self.DayHoursMinus.setText("-")
        self.DayHoursMinus.setObjectName("DayHoursMinus")
        #
        ####### DayBegin set/display #######
        #
        self.DayBeginDisp = QtWidgets.QLabel(self.centralwidget)
        self.DayBeginDisp.setGeometry(QtCore.QRect(700, 420, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.DayBeginDisp.setFont(font)
        self.DayBeginDisp.setObjectName("DayBeginDisp")
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        daybeginvalue = "  " + settings["daybegin"]
        self.DayBeginDisp.setText(daybeginvalue)
        #
        self.DayBeginPlus = QtWidgets.QPushButton(self.centralwidget)
        self.DayBeginPlus.setGeometry(QtCore.QRect(750, 420, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.DayBeginPlus.setFont(font)
        self.DayBeginPlus.setText("+")
        self.DayBeginPlus.setObjectName("DayBeginPlus")
        #
        self.DayBeginMinus = QtWidgets.QPushButton(self.centralwidget)
        self.DayBeginMinus.setGeometry(QtCore.QRect(660, 420, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.DayBeginMinus.setFont(font)
        self.DayBeginMinus.setText("-")
        self.DayBeginMinus.setObjectName("DayBeginMinus")
        #
        ####### Labels #######
        #
        self.MaxTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.MaxTempLabel.setGeometry(QtCore.QRect(660, 80, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MaxTempLabel.setFont(font)
        self.MaxTempLabel.setObjectName("MaxTempLabel")
        self.MinTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.MinTempLabel.setGeometry(QtCore.QRect(660, 160, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MinTempLabel.setFont(font)
        self.MinTempLabel.setObjectName("MinTempLabel")
        self.MaxHumidLabel = QtWidgets.QLabel(self.centralwidget)
        self.MaxHumidLabel.setGeometry(QtCore.QRect(660, 240, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MaxHumidLabel.setFont(font)
        self.MaxHumidLabel.setObjectName("MaxHumidLabel")
        self.DayHoursLabel = QtWidgets.QLabel(self.centralwidget)
        self.DayHoursLabel.setGeometry(QtCore.QRect(660, 320, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DayHoursLabel.setFont(font)
        self.DayHoursLabel.setObjectName("DayHoursLabel")
        self.DayBeginLabel = QtWidgets.QLabel(self.centralwidget)
        self.DayBeginLabel.setGeometry(QtCore.QRect(660, 400, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DayBeginLabel.setFont(font)
        self.DayBeginLabel.setObjectName("DayBeginLabel")
        self.OutTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutTempLabel.setGeometry(QtCore.QRect(10, 136, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.OutTempLabel.setFont(font)
        self.OutTempLabel.setObjectName("OutTempLabel")
        self.OutHumidLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutHumidLabel.setGeometry(QtCore.QRect(10, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.OutHumidLabel.setFont(font)
        self.OutHumidLabel.setObjectName("OutHumidLabel")
        self.InsideTempLabel = QtWidgets.QLabel(self.centralwidget)
        self.InsideTempLabel.setGeometry(QtCore.QRect(10, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.InsideTempLabel.setFont(font)
        self.InsideTempLabel.setObjectName("InsideTempLabel")
        self.InHumidLabel = QtWidgets.QLabel(self.centralwidget)
        self.InHumidLabel.setGeometry(QtCore.QRect(10, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.InHumidLabel.setFont(font)
        self.InHumidLabel.setObjectName("InHumidLabel")
        self.SoilSense4Label = QtWidgets.QLabel(self.centralwidget)
        self.SoilSense4Label.setGeometry(QtCore.QRect(320, 136, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SoilSense4Label.setFont(font)
        self.SoilSense4Label.setObjectName("SoilSense4Label")
        self.SoilSense3Label = QtWidgets.QLabel(self.centralwidget)
        self.SoilSense3Label.setGeometry(QtCore.QRect(320, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SoilSense3Label.setFont(font)
        self.SoilSense3Label.setObjectName("SoilSense3Label")
        self.SoilSense2Label = QtWidgets.QLabel(self.centralwidget)
        self.SoilSense2Label.setGeometry(QtCore.QRect(320, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SoilSense2Label.setFont(font)
        self.SoilSense2Label.setObjectName("SoilSense2Label")
        self.SoilSense1Label = QtWidgets.QLabel(self.centralwidget)
        self.SoilSense1Label.setGeometry(QtCore.QRect(320, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SoilSense1Label.setFont(font)
        self.SoilSense1Label.setObjectName("SoilSense1Label")
        #
        ####### Displays #######
        #
        self.OutTempDisp = QtWidgets.QLabel(self.centralwidget)
        self.OutTempDisp.setGeometry(QtCore.QRect(160, 136, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.OutTempDisp.setFont(font)
        outtemp = str(gh.OutsideTemp()) + " degrees C"
        self.OutTempDisp.setText(outtemp)
        self.OutTempDisp.setObjectName("OutTempDisp")
        #
        self.OutHumidDisp = QtWidgets.QLabel(self.centralwidget)
        self.OutHumidDisp.setGeometry(QtCore.QRect(160, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.OutHumidDisp.setFont(font)
        outhumid = str(gh.OutsideHumidity()) + "% humidity"
        self.OutHumidDisp.setText(outhumid)
        self.OutHumidDisp.setObjectName("OutHumidDisp")
        #
        self.InsideTempDisp = QtWidgets.QLabel(self.centralwidget)
        self.InsideTempDisp.setGeometry(QtCore.QRect(160, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.InsideTempDisp.setFont(font)
        intemp =str(gh.InsideTemp()) + " degrees C"
        self.InsideTempDisp.setText(intemp)
        self.InsideTempDisp.setObjectName("InsideTempDisp")
        #
        self.InHumidDisp = QtWidgets.QLabel(self.centralwidget)
        self.InHumidDisp.setGeometry(QtCore.QRect(160, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.InHumidDisp.setFont(font)
        inhumid = str(gh.InsideHumidity()) + "% humidity"
        self.InHumidDisp.setText(inhumid)
        self.InHumidDisp.setObjectName("InHumidDisp")
        #
        self.SoilSense4Disp = QtWidgets.QLabel(self.centralwidget)
        self.SoilSense4Disp.setGeometry(QtCore.QRect(450, 136, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SoilSense4Disp.setFont(font)
        soilsense4 = str(hd38.soilsensor4())
        self.SoilSense4Disp.setText(soilsense4)
        self.SoilSense4Disp.setObjectName("SoilSense4Disp")
        #
        self.SoilSense2Disp = QtWidgets.QLabel(self.centralwidget)
        self.SoilSense2Disp.setGeometry(QtCore.QRect(450, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SoilSense2Disp.setFont(font)
        soilsense2 = str(hd38.soilsensor2())
        self.SoilSense2Disp.setText(soilsense2)
        self.SoilSense2Disp.setObjectName("SoilSense2Disp")
        #
        self.SoilSense1Disp = QtWidgets.QLabel(self.centralwidget)
        self.SoilSense1Disp.setGeometry(QtCore.QRect(450, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SoilSense1Disp.setFont(font)
        soilsense1 = str(hd38.soilsensor1())
        self.SoilSense1Disp.setText(soilsense1)
        self.SoilSense1Disp.setObjectName("SoilSense1Disp")
        #
        self.SoilSense3Disp = QtWidgets.QLabel(self.centralwidget)
        self.SoilSense3Disp.setGeometry(QtCore.QRect(450, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SoilSense3Disp.setFont(font)
        soilsense3 = str(hd38.soilsensor3())
        self.SoilSense3Disp.setText(soilsense3)
        self.SoilSense3Disp.setObjectName("SoilSense3Disp")
        #
        self.btnAutoMan = QtWidgets.QPushButton(self.centralwidget)
        self.btnAutoMan.setGeometry(QtCore.QRect(10, 190, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnAutoMan.setCheckable(True)
        self.btnAutoMan.setFont(font)
        self.btnAutoMan.setObjectName("btnAutoMan")
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        currentvalue = settings["automan"]
        if currentvalue == "1":
            self.btnAutoMan.setChecked(True)
            self.btnAutoMan.setText("AUTO")
        else:
            self.btnAutoMan.setChecked(False)
            self.btnAutoMan.setText("MANUAL")
        #
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(10, 0, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
        self.btnExit.setText("Exit Program")
        #
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(650, 4, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setObjectName("btnUpdate")
        #
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-40, 170, 691, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(640, 80, 20, 101))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(647, 70, 251, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.Relay01.clicked.connect(self.actionRelay1)
        self.Relay02.clicked.connect(self.actionRelay2)
        self.Relay03.clicked.connect(self.actionRelay3)
        self.Relay04.clicked.connect(self.actionRelay4)
        self.Relay05.clicked.connect(self.actionRelay5)
        self.Relay06.clicked.connect(self.actionRelay6)
        self.Relay07.clicked.connect(self.actionRelay7)
        self.Relay08.clicked.connect(self.actionRelay8)
        self.Relay09.clicked.connect(self.actionRelay9)
        self.Relay10.clicked.connect(self.actionRelay10)
        self.Relay11.clicked.connect(self.actionRelay11)
        self.Relay12.clicked.connect(self.actionRelay12)
        self.Relay13.clicked.connect(self.actionRelay13)
        self.Relay14.clicked.connect(self.actionRelay14)
        self.Relay15.clicked.connect(self.actionRelay15)
        self.Relay16.clicked.connect(self.actionRelay16)
        self.SliderSet.clicked.connect(self.actionSetSlider)
        self.MaxTempPlus.clicked.connect(self.actionMaxTempPlus)
        self.MaxTempMinus.clicked.connect(self.actionMaxTempMinus)
        self.MinTempPlus.clicked.connect(self.actionMinTempPlus)
        self.MinTempMinus.clicked.connect(self.actionMinTempMinus)
        self.MaxHumidPlus.clicked.connect(self.actionMaxHumidPlus)
        self.MaxHumidMinus.clicked.connect(self.actionMaxHumidMinus)
        self.DayHoursPlus.clicked.connect(self.actionDayHoursPlus)
        self.DayHoursMinus.clicked.connect(self.actionDayHoursMinus)
        self.DayBeginPlus.clicked.connect(self.actionDayBeginPlus)
        self.DayBeginMinus.clicked.connect(self.actionDayBeginMinus)
        self.btnUpdate.clicked.connect(self.actionUpdate)
        self.btnAutoMan.clicked.connect(self.actionAutoMan)
        self.btnExit.clicked.connect(lambda:self.close())

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MaxTempLabel.setText(_translate("MainWindow", "Max Temp:"))
        self.MinTempLabel.setText(_translate("MainWindow", "Min Temp:"))
        self.MaxHumidLabel.setText(_translate("MainWindow", "Max Humid:"))
        self.DayHoursLabel.setText(_translate("MainWindow", "Day Hours:"))
        self.DayBeginLabel.setText(_translate("MainWindow", "Day Begin:"))
        self.OutTempLabel.setText(_translate("MainWindow", "Outside Temp:"))
        self.OutHumidLabel.setText(_translate("MainWindow", "Outside Humid:"))
        self.InsideTempLabel.setText(_translate("MainWindow", "Inside Temp:"))
        self.InHumidLabel.setText(_translate("MainWindow", "Inside Humid:"))
        self.btnUpdate.setText(_translate("MainWindow", "UPDATE"))
        self.SoilSense4Label.setText(_translate("MainWindow", "Soil Sensor 4"))
        self.SoilSense3Label.setText(_translate("MainWindow", "Soil Sensor 3:"))
        self.SoilSense2Label.setText(_translate("MainWindow", "Soil Sensor 2:"))
        self.SoilSense1Label.setText(_translate("MainWindow", "Soil Sensor 1:"))

    def actionEnableRelays(self):
        self.Relay01.setEnabled(True)
        self.Relay02.setEnabled(True)
        self.Relay03.setEnabled(True)
        self.Relay04.setEnabled(True)
        self.Relay05.setEnabled(True)
        self.Relay06.setEnabled(True)
        self.Relay07.setEnabled(True)
        self.Relay08.setEnabled(True)
        self.Relay09.setEnabled(True)
        self.Relay10.setEnabled(True)
        self.Relay11.setEnabled(True)
        self.Relay12.setEnabled(True)
        self.Relay13.setEnabled(True)
        self.Relay14.setEnabled(True)
        self.Relay15.setEnabled(True)
        self.Relay16.setEnabled(True)

    def actionDisableRelays(self):
        self.Relay01.setEnabled(False)
        self.Relay02.setEnabled(False)
        self.Relay03.setEnabled(False)
        self.Relay04.setEnabled(False)
        self.Relay05.setEnabled(False)
        self.Relay06.setEnabled(False)
        self.Relay07.setEnabled(False)
        self.Relay08.setEnabled(False)
        self.Relay09.setEnabled(False)
        self.Relay10.setEnabled(False)
        self.Relay11.setEnabled(False)
        self.Relay12.setEnabled(False)
        self.Relay13.setEnabled(False)
        self.Relay14.setEnabled(False)
        self.Relay15.setEnabled(False)
        self.Relay16.setEnabled(False)

    def actionAutoMan(self):
        if self.btnAutoMan.isChecked():
            self.btnAutoMan.setText("AUTO")
            with open("GHsettings.json") as f:
                settings = json.load(f)
            settings["automan"] = "1"
            with open("GHsettings.json","w+") as f:
                json.dump(settings, f)
            self.actionDisableRelays()
        else:
            self.btnAutoMan.setText("MANUAL")
            with open("GHsettings.json") as f:
                settings = json.load(f)
            settings["automan"] = "0"
            with open("GHsettings.json","w+") as f:
                json.dump(settings, f)
            self.actionEnableRelays()

    def actionUpdate(self):
        outtempupdate = str(gh.OutsideTemp()) + " degrees C"
        outhumidupdate = str(gh.OutsideHumidity()) + "% humidity"
        intempupdate = str(gh.InsideTemp()) + " degrees C"
        inhumidupdate = str(gh.InsideHumidity()) + "% humidity"
        soilsensor1update = str(hd38.soilsensor1())
        soilsensor2update = str(hd38.soilsensor2())
        soilsensor3update = str(hd38.soilsensor3())
        soilsensor4update = str(hd38.soilsensor4())
        self.OutTempDisp.setText(outtempupdate)
        self.OutHumidDisp.setText(outhumidupdate)
        self.InsideTempDisp.setText(intempupdate)
        self.InHumidDisp.setText(inhumidupdate)
        self.SoilSense1Disp.setText(soilsensor1update)
        self.SoilSense2Disp.setText(soilsensor2update)
        self.SoilSense3Disp.setText(soilsensor3update)
        self.SoilSense4Disp.setText(soilsensor4update)


    def actionRelay1(self):
        if self.Relay01.isChecked():
            self.Relay01.setText("Cool H2O ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay1"] = "1"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.onrelay1()
        else:
            self.Relay01.setText("Cool H2O OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay1"] = "0"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.offrelay1()

    def actionRelay2(self):
        if self.Relay02.isChecked():
            self.Relay02.setText("Extra 1 ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay2"] = "1"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.onrelay2()
        else:
            self.Relay02.setText("Extra 1 OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay2"] = "0"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.offrelay2()

    def actionRelay3(self):
        if self.Relay03.isChecked():
            self.Relay03.setText("Extra 2 ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay3"] = "1"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.onrelay3()
        else:
            self.Relay03.setText("Extra 2 OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay3"] = "0"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.offrelay3()

    def actionRelay4(self):
        if self.Relay04.isChecked():
            self.Relay04.setText("Extra 3 ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay4"] = "1"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.onrelay4()
        else:
            self.Relay04.setText("Extra 3 OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay4"] = "0"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.offrelay4()

    def actionRelay5(self):
        if self.Relay05.isChecked():
            self.Relay05.setText("Fans 1 ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay5"] = "1"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.onrelay5()
        else:
            self.Relay05.setText("Fans 1 OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay5"] = "0"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.offrelay5()

    def actionRelay6(self):
        if self.Relay06.isChecked():
            self.Relay06.setText("Fans 2 ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay6"] = "1"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.onrelay6()
        else:
            self.Relay06.setText("Fans 2 OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay6"] = "0"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.offrelay6()

    def actionRelay7(self):
        if self.Relay07.isChecked():
            self.Relay07.setText("Up Fans ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay7"] = "1"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.onrelay7()
        else:
            self.Relay07.setText("Up Fans OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay7"] = "0"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.offrelay7()

    def actionRelay8(self):
        if self.Relay08.isChecked():
            self.Relay08.setText("Vents ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay8"] = "1"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.onrelay8()
        else:
            self.Relay08.setText("Vents OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay8"] = "0"
            with open("GHsettings.json","w+") as f:# open user dictionary
                json.dump(settings, f)
            gh.offrelay8()

    def actionRelay9(self):
        if self.Relay09.isChecked():
            self.Relay09.setText("Heaters ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay9"] = "1"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.onrelay9()
        else:
            self.Relay09.setText("Heaters OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay9"] = "0"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.offrelay9()

    def actionRelay10(self):
        if self.Relay10.isChecked():
            self.Relay10.setText("Dehumid ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay10"] = "1"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.onrelay10()
        else:
            self.Relay10.setText("Dehumid OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay10"] = "0"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.offrelay10()

    def actionRelay11(self):
        if self.Relay11.isChecked():
            self.Relay11.setText("Lights 1 ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay11"] = "1"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.onrelay11()
        else:
            self.Relay11.setText("Lights 1 OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay11"] = "0"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.offrelay11()

    def actionRelay12(self):
        if self.Relay12.isChecked():
            self.Relay12.setText("Lights 2 ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay12"] = "1"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.onrelay12()
        else:
            self.Relay12.setText("Lights 2 OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay12"] = "0"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.offrelay12()

    def actionRelay13(self):
        if self.Relay13.isChecked():
            self.Relay13.setText("Drip 1 ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay13"] = "1"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.onrelay13()
        else:
            self.Relay13.setText("Drip 1 OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay13"] = "0"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.offrelay13()

    def actionRelay14(self):
        if self.Relay14.isChecked():
            self.Relay14.setText("Drip 2 ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay14"] = "1"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.onrelay14()
        else:
            self.Relay14.setText("Drip 2 OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay14"] = "0"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.offrelay14()

    def actionRelay15(self):
        if self.Relay15.isChecked():
            self.Relay15.setText("Drip 3 ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay15"] = "1"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.onrelay15()
        else:
            self.Relay15.setText("Drip 3 OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay15"] = "0"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.offrelay15()

    def actionRelay16(self):
        if self.Relay16.isChecked():
            self.Relay16.setText("Drip 4 ON")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay16"] = "1"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.onrelay16()
        else:
            self.Relay16.setText("Drip 4 OFF")
            with open("GHsettings.json",) as f:
                settings = json.load(f)
            settings["relay16"] = "0"
            with open("GHsettings.json","w+") as f:# open settings file
                json.dump(settings, f)
            gh.offrelay16()

    def actionSetSlider(self):
        angle = self.Slider.value()
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        settings["slider"] = angle
        with open("GHsettings.json","w+") as f:# open settings file
            json.dump(settings, f)
        print("Cooler wall angle set", angle)

    def actionMaxTempPlus(self):
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        value = int(settings["maxtemp"]) + 1
        maxtempvalue = " " + str(value)
        self.MaxTempDisp.setText(maxtempvalue)
        settings["maxtemp"] = maxtempvalue
        with open("GHsettings.json","w+") as f:# open settings file
            json.dump(settings, f)

    def actionMaxTempMinus(self):
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        value = int(settings["maxtemp"]) - 1
        maxtempvalue = " " + str(value)
        self.MaxTempDisp.setText(maxtempvalue)
        settings["maxtemp"] = maxtempvalue
        with open("GHsettings.json","w+") as f:# open settings file
            json.dump(settings, f)

    def actionMinTempPlus(self):
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        value = int(settings["mintemp"]) + 1
        mintempvalue = " " + str(value)
        self.MinTempDisp.setText(mintempvalue)
        settings["mintemp"] = mintempvalue
        with open("GHsettings.json","w+") as f:# open settings file
            json.dump(settings, f)

    def actionMinTempMinus(self):
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        value = int(settings["mintemp"]) - 1
        mintempvalue = " " + str(value)
        self.MinTempDisp.setText(mintempvalue)
        settings["mintemp"] = mintempvalue
        with open("GHsettings.json","w+") as f:# open settings file
            json.dump(settings, f)

    def actionMaxHumidPlus(self):
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        value = int(settings["maxhumid"]) + 1
        maxhumidvalue = " " + str(value)
        self.MaxHumidDisp.setText(maxhumidvalue)
        settings["maxhumid"] = maxhumidvalue
        with open("GHsettings.json","w+") as f:# open settings file
            json.dump(settings, f)

    def actionMaxHumidMinus(self):
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        value = int(settings["maxhumid"]) - 1
        maxhumidvalue = " " + str(value)
        self.MaxHumidDisp.setText(maxhumidvalue)
        settings["maxhumid"] = maxhumidvalue
        with open("GHsettings.json","w+") as f:# open settings file
            json.dump(settings, f)

    def actionDayHoursPlus(self):
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        value = int(settings["dayhours"]) + 1
        dayhoursvalue = " " + str(value)
        self.DayHoursDisp.setText(dayhoursvalue)
        settings["dayhours"] = dayhoursvalue
        with open("GHsettings.json","w+") as f:# open settings file
            json.dump(settings, f)

    def actionDayHoursMinus(self):
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        value = int(settings["dayhours"]) - 1
        dayhoursvalue = " " + str(value)
        self.DayHoursDisp.setText(dayhoursvalue)
        settings["dayhours"] = dayhoursvalue
        with open("GHsettings.json","w+") as f:# open settings file
            json.dump(settings, f)

    def actionDayBeginPlus(self):
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        value = int(settings["daybegin"]) + 1
        daybeginvalue = " " + str(value)
        self.DayBeginDisp.setText(daybeginvalue)
        settings["daybegin"] = daybeginvalue
        with open("GHsettings.json","w+") as f:# open settings file
            json.dump(settings, f)

    def actionDayBeginMinus(self):
        with open("GHsettings.json",) as f:
            settings = json.load(f)
        value = int(settings["daybegin"]) - 1
        daybeginvalue = " " + str(value)
        self.DayBeginDisp.setText(daybeginvalue)
        settings["daybegin"] = daybeginvalue
        with open("GHsettings.json","w+") as f:# open settings file
            json.dump(settings, f)
