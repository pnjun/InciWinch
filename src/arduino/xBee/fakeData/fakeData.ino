#include <SoftwareSerial.h>
#include <XBee.h>
#include <Printers.h>

//Start values for fake data (speed&height)
float IAS = 10;
float HEI = 10;

//Destination address 
//#define DEST_LOW 0x0013A200
//#define DEST_HI  0x417FE5ED

#define DEST_LOW 0x0
#define DEST_HI  0x0000FFFF

//Global xbee and serial handle
XBee xbee = XBee();
SoftwareSerial mySerial(10, 11); // RX, TX

void setup()
{
  // Serial setup
  mySerial.begin(9600);
  while (!mySerial) continue;

  //Serial.begin(9600);
  //while (!Serial) continue;

  // xBee API setup
  xbee.setSerial(Serial);

  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  IAS += 0.4;
  HEI += 2;
  digitalWrite(LED_BUILTIN, HIGH);
  // Construct json by hand
  String json = String( "{\"IAS\":" + String(IAS) + ",\"HEI\":" + String(HEI) + "}" );

  uint8_t payload[json.length() + 1]; //The +1 is there because the string is null terminated 
  json.toCharArray(payload, json.length() + 1); 

  // Send data
  XBeeAddress64 addr64 = XBeeAddress64(DEST_LOW, DEST_HI);
  ZBTxRequest zbTx = ZBTxRequest(addr64, payload, json.length());
  xbee.send(zbTx);
  digitalWrite(LED_BUILTIN, LOW);
  // Wait for next cycle
  delay(1000);
}
