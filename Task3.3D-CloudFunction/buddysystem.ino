// pin where the LED is connected to
const pin_t LED = D3;
// RIOT of photon buddy that detects waving motion
const char *Event = "Deakin_RIOT_SIT210_Photon_Buddy";

void setup()
{
    // declare the pin as output pin
	pinMode(LED, OUTPUT);
    // subscribe to the RIOT
	Particle.subscribe(Event, handler);
}


void handler(const char *event, const char *data)
{
    // if waving motion is detected
    if (strcmp(data,"wave") == 0)
    {
        blink(3,500);
    }
}

// function for blinking the LED
void blink(int blinks, int interval)
{
    for(int i = 0; i < blinks; i++)
    {
        digitalWrite(LED, HIGH);
        delay(interval);
        digitalWrite(LED, LOW);
        delay(interval);
    }
}
