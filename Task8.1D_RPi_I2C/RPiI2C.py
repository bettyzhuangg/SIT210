from time import sleep 
from gpiozero import DistanceSensor
from signal import signal, SIGTERM, SIGHUP, pause


sensor = DistanceSensor(echo = 21, trigger = 20)

while True:
    distance = sensor.value
    print("distance:")
    print(distance)
    
    # between 0 to 0.25
    if distance < 0.25 and distance > 0 1:
        print("Object blocked sensor")
    # between 0.25 to 0.5
    elif distance < 0.5 and distance >= 0.25:
        print("Object is very close")
    # between 0.5 to 0.75
    elif distance < 0.75 and distance >= 0.5:
        print("Object is close")    
    # between 0.75 to 1
    elif distance < 1 and distance >= 0.75:
        print("Object is nearby")
    # greater than 1
    else:
        print("No object nearby")
    sleep(1)
