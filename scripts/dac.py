#!/usr/bin/python3

# Main script for DAC setup
# Inputs - 3 args:
#   DAC number - (0,1,2)
#   Internal DAC number - (0,1)
#   value to be written - (0-255) 

import sys
import spidev
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# input arguments validation
if (len(sys.argv) != 4):
    print("invalid number of arguments")
    quit()
if (int(sys.argv[1]) > 2 or int(sys.argv[1]) < 0):
    print("invalid DAC number")
    quit()
if (not (int(sys.argv[2]) == 0 or int(sys.argv[2]) == 1)):
    print("invalid internal DAC number")
    quit()
if (int(sys.argv[3]) > 255 or int(sys.argv[3]) < 0):
    print("value not in range 0-255")
    quit()

# latPin
latPin = 13

# bring lat high
GPIO.setup(latPin, GPIO.OUT)
GPIO.output(latPin, GPIO.HIGH)

# spi setup
spi = spidev.SpiDev()
spi.open(1, 0)
spi.max_speed_hz = 10000

# GPIO setup
GPIO.setmode(GPIO.BOARD)
dac = [37, 22, 18]

# bring cs low
GPIO.setup(dac[int(sys.argv[1])], GPIO.OUT)
GPIO.output(dac[int(sys.argv[1])], GPIO.LOW)

# send data
spi.xfer([int(sys.argv[2])*8, 0x00, int(sys.argv[3])])

# bring cs high
GPIO.output(dac[int(sys.argv[1])], GPIO.HIGH)

# bring lat low
GPIO.output(latPin, GPIO.LOW)
GPIO.output(latPin, GPIO.HIGH)
