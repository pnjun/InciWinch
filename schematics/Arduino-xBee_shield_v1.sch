EESchema Schematic File Version 2
LIBS:arduino
LIBS:XB8X-DMUS-001
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:Arduino-xBee_shield_v1-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	6400 3200 7500 3200
Wire Wire Line
	3800 3700 3600 3700
Wire Wire Line
	3800 3900 3400 3900
Wire Wire Line
	3400 3900 3400 1900
Wire Wire Line
	3400 1900 7600 1900
Wire Wire Line
	7500 3200 7500 2400
Wire Wire Line
	7500 2400 7700 2400
Wire Wire Line
	7400 3100 7400 2300
Wire Wire Line
	7400 2300 7700 2300
Wire Wire Line
	6400 3100 7400 3100
Wire Wire Line
	3600 2100 7700 2100
Wire Wire Line
	7600 1900 7600 2200
Wire Wire Line
	7600 2200 7700 2200
Wire Wire Line
	6400 2300 7200 2300
Wire Wire Line
	6400 2400 7100 2400
$Comp
L Conn_01x02 J2
U 1 1 5B13EDA9
P 7200 4900
F 0 "J2" H 7200 5000 50  0000 C CNN
F 1 "LX Serial " H 7200 4700 50  0000 C CNN
F 2 "Socket_Strips:Socket_Strip_Straight_1x02_Pitch2.54mm" H 7200 4900 50  0001 C CNN
F 3 "" H 7200 4900 50  0001 C CNN
	1    7200 4900
	0    1    1    0   
$EndComp
$Comp
L Conn_01x02 J1
U 1 1 5B13EEDB
P 3700 4900
F 0 "J1" H 3700 5000 50  0000 C CNN
F 1 "Power In" H 3700 4700 50  0000 C CNN
F 2 "Socket_Strips:Socket_Strip_Straight_1x02_Pitch2.54mm" H 3700 4900 50  0001 C CNN
F 3 "" H 3700 4900 50  0001 C CNN
	1    3700 4900
	0    1    1    0   
$EndComp
Wire Wire Line
	7100 2400 7100 4700
Wire Wire Line
	10300 4400 10300 3900
Wire Wire Line
	10300 3900 10100 3900
Wire Wire Line
	7200 2300 7200 4700
Wire Wire Line
	6750 4700 6750 3100
Connection ~ 6750 3100
$Comp
L XB8X-DMUS-001 xBee1
U 1 1 5B13E865
P 7700 2100
F 0 "xBee1" H 9950 2400 50  0000 L CNN
F 1 "xBee SX 868" H 9950 2300 50  0000 L CNN
F 2 "XB8X-DMUS-001:XBP9XDMRS001" H 9950 2200 50  0001 L CNN
F 3 "https://www.digi.com/pdf/ds_xbee-sx-868.pdf" H 9950 2100 50  0001 L CNN
F 4 "RF Modules XBee SX 868, 25mW DigiMesh, U.FL" H 9950 2000 50  0001 L CNN "Description"
F 5 "12" H 9950 1900 50  0001 L CNN "Height"
F 6 "Digi International" H 9950 1800 50  0001 L CNN "Manufacturer_Name"
F 7 "XB8X-DMUS-001" H 9950 1700 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "XB8X-DMUS-001" H 9950 1400 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/xb8x-dmus-001/digi-international" H 9950 1300 50  0001 L CNN "Arrow Price/Stock"
	1    7700 2100
	1    0    0    -1  
$EndComp
$Comp
L Arduino_Nano_Socket Arduino1
U 1 1 5B13DE08
P 5100 3200
F 0 "Arduino1" V 5200 3200 60  0000 C CNN
F 1 "Arduino_Nano_Socket" V 5000 3200 60  0000 C CNN
F 2 "Arduino:Arduino_Nano_Socket" H 6900 6950 60  0001 C CNN
F 3 "" H 6900 6950 60  0001 C CNN
	1    5100 3200
	1    0    0    -1  
$EndComp
$Comp
L Conn_01x02 J3
U 1 1 5B1C13C9
P 6750 4900
F 0 "J3" H 6750 5000 50  0000 C CNN
F 1 "xBee Serial" H 6750 4700 50  0000 C CNN
F 2 "Socket_Strips:Socket_Strip_Straight_1x02_Pitch2.54mm" H 6750 4900 50  0001 C CNN
F 3 "" H 6750 4900 50  0001 C CNN
	1    6750 4900
	0    1    1    0   
$EndComp
Wire Wire Line
	6650 4700 6650 3200
Connection ~ 6650 3200
Wire Wire Line
	3800 4100 3700 4100
Wire Wire Line
	3700 4100 3700 4700
Wire Wire Line
	3600 2100 3600 4700
Wire Wire Line
	3600 3800 3800 3800
Wire Wire Line
	10300 4400 3600 4400
Connection ~ 3600 4400
Connection ~ 3600 3700
Connection ~ 3600 3800
$EndSCHEMATC
