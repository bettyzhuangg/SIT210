from time import sleep
import time
import gpiozero
from gpiozero import Buzzer
from gpiozero import Button
import requests
import datetime

button = Button(22)
def send_mess(time):
    conversion = str(datetime.timedelta(seconds=round(time)))
    r=requests.post("https://maker.ifttt.com/trigger/time/json/with/key/dWmKMQJ5Up6ck-uFPfMeuU", json={"Study for":conversion})
i=3

while True:
    if(button.is_pressed and i%2!=0):
        start = time.time()
        i+=1
        print("START"+str(i))
    elif(button.is_pressed and i%2==0):
        end = time.time()
        print("END"+str(i))
        print(end - start)
        send_mess(end-start)
        i+=1
