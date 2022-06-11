import sys
import time
import requests
# Make sure you install required libraries:
# https://gpiozero.readthedocs.io/en/stable/installing.html
import gpiozero

# change this value based on which GPIO port the relay is connected to
RELAY_PIN = 18

# create a relay object.
# Triggered by the output pin going low: active_high=False.
# Initially off: initial_value=False
relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)


def set_relay(status):
    if status:
        print("Setting relay: ON")
        relay.on()
    else:
        print("Setting relay: OFF")
        relay.off()


def toggle_relay():
    print("toggling relay")
    relay.toggle()


def main_loop():
    # start by turning the relay off
    set_relay(False)
    while 1:
        # then toggle the relay every second until the app closes
        r=requests.get("http://128.199.190.200/?temp=1")
        if(float(r.text)<13):
            relay.on()
        else:
            relay.off()
        time.sleep(1)


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        # turn the relay off
        #set_relay(False)
        relay.off()
        print("\nExiting application\n")
        # exit the application
        sys.exit(0)
