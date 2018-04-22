#include <ArduinoJson.h>

// WARING: does not compile for arduino 2009

#define AIRCRAFT_ID "TEST_PLANE"

void setup()
{
  // Serial setup
  Serial.begin(9600);
  while (!Serial) continue;
}

void loop() {
  // Json library buffer, sets the amount of memory reserved for Json construction
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& data = jsonBuffer.createObject();

  data['ID'] = AIRCRAFT_ID;
  data['IAS'] = 50;
  data['HEI'] = 350;

  data.printTo(Serial);
  Serial.print('\n');

  delay(500);
}
