#!/usr/bin/python3
import spidev
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# spi setup
spi = spidev.SpiDev()
spi.open(1, 0)
spi.max_speed_hz = 10000

# GPIO setup
GPIO.setmode(GPIO.BOARD)
dac = [37, 22, 18]

# data setup
reference = [0x08*8, 0x00, 0x05]
powerDown = [0x09*8, 0x00, 0x00]


# set each CS to HIGH
for i in range(len(dac)):
    GPIO.setup(dac[i], GPIO.OUT)
    GPIO.output(dac[i], GPIO.HIGH)
    
# program the DACs

for i in range(len(dac)):
    GPIO.output(dac[i], GPIO.LOW)
    
    spi.xfer(powerDown.copy())
    spi.xfer(reference.copy())
    
    GPIO.output(dac[i], GPIO.HIGH)
