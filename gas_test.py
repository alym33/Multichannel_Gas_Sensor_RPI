#from machine import I2C
import RPi.GPIO as GPIO
import smbus
#from board import I2C
import board
#import busio
#from adafruit_bus_device.i2c_device import I2CDevice
import time

#i2c = busio.I2C(3, 2) #frequency=30000)#I2C()
#time.sleep(1)
from gas import Gas
i2c = smbus.SMBus(1)
time.sleep(1)
g = Gas(i2c)
g.gas_dump()
