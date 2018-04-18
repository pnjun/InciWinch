
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3); // RX, TX
int incomingByte = 0;

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  if (mySerial.available() > 0)
  {
     incomingByte = mySerial.read();
     Serial.write(incomingByte);
  }
  if (Serial.available() > 0)
  {
     incomingByte = Serial.read();
     mySerial.write(incomingByte);
  }

}
