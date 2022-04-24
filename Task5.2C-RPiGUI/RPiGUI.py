from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led1 = LED(2)
led2 = LED(3)
led3 = LED(4)

box = Tk()
box.title("LED Control System")
Font = tkinter.font.Font(family = "Arial", size = 12, weight = "bold")

def controlLED1():
    if led1.is_lit:
        led1.off()
        button1["text"] = "ON"
        
    else:
        led1.on()
        button1["text"] = "OFF"
        

def controlLED2():
    if led2.is_lit:
        led2.off()
        button2["text"] = "ON"
        
    else:
        led2.on()
        button2["text"] = "OFF"
        

def controlLED3():
    if led3.is_lit:
        led3.off()
        button3["text"] = "ON"
        
    else:
        led3.on()
        button3["text"] = "OFF"

button1 = Button(box, text = "RED", font = Font, command = controlLED1, bg="red", height = 2, width = 48)
button1.grid(row=0, column=1)

button2 = Button(box, text = "GREEN", font = Font, command = controlLED2, bg="green", height = 2, width = 48)
button2.grid(row=0, column=2)

button3 = Button(box, text = "YELLOW", font = Font, command = controlLED3, bg="yellow", height = 2, width = 48)
button3.grid(row=0, column=3)
