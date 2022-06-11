#!/usr/bin/python
import smbus
import time
import requests
import RPi.GPIO as GPIO
import requests

channel = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

DEVICE     = 0x23
ONE_TIME_HIGH_RES_MODE = 0x20
 
bus = smbus.SMBus(1)
 
def convertToNumber(data):
  return ((data[1] + (256 * data[0])) / 1.2)
 
def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
  return convertToNumber(data)
 
def main():
 
  while True:
    r=requests.get('http://128.199.190.200/index.php?light=1')
    print(r.text)
    try:
        x=float(r.text)
        x = readLight()
        print("light: " + str(x))
        pload = {'light':x}
        r = requests.post('http://128.199.190.200/index.php', data=pload)
        time.sleep(2)
    except ValueError:
        time.sleep(2)
        print("Sensor failure, check wiring")
 
if __name__=="__main__":
   main()

