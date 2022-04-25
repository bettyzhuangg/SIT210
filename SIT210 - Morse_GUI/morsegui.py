from tkinter import *
from time import sleep
from tkinter import messagebox
import RPi.GPIO as GPIO

RPi.GIPO.setmode(RPi.GPIO.BCM)

led = LED(2)

win = Tk()
win.title("Blink Morse Code")
Font = tkinter.font.Font(family = "Arial", size = 12, weight = "bold")

MORSE_CODEDICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encode(msg):
    code = ''
    for char in msg:
      if char == ' ':
        code += ' '
      else:
        code += MORSECODE_DICT[char] + ' '
    return code
  
def blinkLED():
    msg = input.get.upper()[:12]
    print(msg)
    morseCode = encode(msg)
    print(morseCode)
    print(len(morseCode))
    for i in range(0, len(morseCode)):
      if(morseCode[i]=="."):
        print(".")
        led.on()
        time.sleep(0.4)
        led.off()
      elif(morseCode[i]=="-"):
        print("-")
        led.on()
        time.sleep(1.2)
        led.off()
      else:
        print(" ")
        time.sleep(0.4)
            
input = Entry(win, width = 50)
input.pack()

button_container = Frame(win)
button_container.pack()

button = Button(button_container, text = "Blink morse code", command = blinkLED) 
button.grid(row=0, column=0

mainloop()
