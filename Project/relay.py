import sys
import time
import requests
import gpiozero

RELAY_PIN = 18

relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

def main_loop():
    relay.off()
    while 1:
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
