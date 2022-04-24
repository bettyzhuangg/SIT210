from time import sleep 
from gpiozero import DistanceSensor, PWMLED
from signal import signal, SIGTERM, SIGHUP, pause

led = PWMLED(14)
sensor = DistanceSensor(echo = 21, trigger = 20)

led.on()
while True:
    distance = sensor.value
    intensity = round (1.0 - distance, 1)
    
    if intensity < 0:
        intensity = 0.0
    led.value = intensity
    
    print("distance:")
    print(distance)
    print("LED intensity:")
    print(intensity)
    
    sleep(0.1)        
