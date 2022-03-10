#include "PietteTech_DHT.h" 

#define DHTTYPE  DHT22       // Sensor type DHT11/21/22/AM2301/AM2302
#define DHTPIN   D2      // Digital pin for communications


PietteTech_DHT DHT(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(9600);
  while (!Serial.available() && millis() < 30000) {
    Particle.process();
    delay(1000);
  }

  DHT.begin();
}

void loop()
{
  int result = DHT.acquireAndWait(1000); // wait up to 1 sec (default indefinitely)

  float tempe = DHT.getCelsius();
  String temp = String(tempe);
  Particle.publish("temperature", temp, PRIVATE);

  delay(30000);
}

