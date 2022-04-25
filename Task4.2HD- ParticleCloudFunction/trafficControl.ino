int redLED = D2;
int greenLED = D5;
int yellowLED = D8;


void setup()
{
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);

}

void loop()
{
    Particle.function("traffic_control",controlLED);
}

int controlLED(String command) 
{

    if (command=="red") {
        digitalWrite(redLED, HIGH);
        digitalWrite(greenLED, LOW);
        digitalWrite(yellowLED, LOW);
        return 1;
    }
    else if (command=="green") {
        digitalWrite(redLED, LOW);
        digitalWrite(greenLED, HIGH);
        digitalWrite(yellowLED, LOW);
        return 2;
    }
    else if (command=="yellow") {
        digitalWrite(redLED, LOW);
        digitalWrite(greenLED, LOW);
        digitalWrite(yellowLED, HIGH);
        return 3;
    }
    else if (command=="off") {
        digitalWrite(redLED, LOW);
        digitalWrite(greenLED, LOW);
        digitalWrite(yellowLED, LOW);
        return 0;
    }
    else {
        return -1;
    }
}
