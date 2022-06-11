from time import sleep
import gpiozero
import requests

led = gpiozero.PWMLED(14)
while True:
    r=requests.get('http://128.199.190.200/index.php?light=1')
    print("light: " + r.text)
    x=float(r.text)
    val = 1-x/1000
    if val > 0.9:
        val = x
        led.on()
        led.value = val
    else:
        led.off()
