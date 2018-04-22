
#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX
int incomingByte = 0;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  mySerial.begin(9600);

  mySerial.print("+++");
}

// the loop function runs over and over again forever
void loop() {
  if (mySerial.available() > 0)
  {
     digitalWrite(LED_BUILTIN, HIGH);
     delay(10);
     digitalWrite(LED_BUILTIN, LOW);

     incomingByte = mySerial.read();
     Serial.write(incomingByte);
  }
  if (Serial.available() > 0)
  {
     incomingByte = Serial.read();
     mySerial.write(incomingByte);
  }

}
