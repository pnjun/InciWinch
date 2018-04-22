#include <Printers.h>
#include <XBee.h>

// Simplified version for arduino 2009

//Start values for fake data (speed&height)
float IAS = 70;
float HEI = 356;

//Destination address (set to zero since we want to talk to the PAN coordinator)
#define DEST_LOW 0x0
#define DEST_HI  0x0

//Global xbee handle
XBee xbee = XBee();

void setup()
{
  // Serial setup
  Serial.begin(9600);
  while (!Serial) continue;

  // xBee API setup
  xbee.setSerial(Serial);
}

void loop() {
  IAS += 0.4;
  HEI += 2;

  // Construct json by hand
  String json = String( "{ID:'TEST_PLANE','IAS':" + String(IAS) + ",'HEI':" + String(HEI) + "}" );

  uint8_t payload[json.length() + 1]; //The +1 is there because the string is null terminated 
  json.toCharArray(payload, json.length() + 1); 

  // Send data
  XBeeAddress64 addr64 = XBeeAddress64(DEST_LOW, DEST_HI);
  ZBTxRequest zbTx = ZBTxRequest(addr64, payload, json.length());
  xbee.send(zbTx);
 
  // Wait for next cycle
  delay(500);
}
