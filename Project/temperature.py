import Adafruit_DHT
import time
import requests

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 10
 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temperature: " + str(temperature))
        pload = {'temp':temperature}
        r = requests.post('http://128.199.190.200/index.php', data=pload)
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(2);
