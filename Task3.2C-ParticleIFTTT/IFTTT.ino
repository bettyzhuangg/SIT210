// output pin for LED light
int LED_PIN = D6;

// input pin for sensing light
int SENSOR_PIN = A0;

// value read by the sensor
int analogvalue;


void setup()
{
    // declare the input and output pins
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, HIGH);
}

void loop()
{
    // read the value from the phototransistor and save it to the associated variable
    analogvalue = analogRead(SENSOR_PIN);

    // if sunlight is detected
    if (analogvalue > 15)
    {
        // for validation and test case purposes: turn on the LED
        digitalWrite(LED_PIN, HIGH);
        // send the message to the cloud that sunlight exposure is detected
        Particle.publish("sunlight_exposure","positive");
    }
    // else if sunlight is not detected
    else
    {
        // for validation and test case purposes: turn off the LED
        digitalWrite(LED_PIN, LOW);
        // send the message to the cloud that sunlight exposure is not detected
        Particle.publish("sunlight_exposure","negative");
    }

    // to prevent overflowing the serial buffer
    delay(1000ms);
}
