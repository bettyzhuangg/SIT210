from time import sleep
import gpiozero
import requests

ultrasonic = gpiozero.DistanceSensor(echo=17, trigger=4)
buzzer = Buzzer(27)

while True:
    distance= round(ultrasonic.value,2)
    sleep(0.1)
    if distance < 0.51:
        print(str(distance)+"m ")
        buzzer.on()
        sleep(0.5)
        buzzer.off()
        sleep(0.5)
    else:
        buzzer.off()
