#include <SoftwareSerial.h>
#include <XBee.h>
#include <Printers.h>

// Destination address (set to zero since we want to talk to the PAN coordinator)
#define DEST_LOW 0x0
#define DEST_HI  0x0

// Serials and xbee handle (standard serial is unused for USB debug purposes)
SoftwareSerial mySerial(10, 11); // RX, TX
SoftwareSerial lxSerial(2, 3); // RX, TX
XBee xbee = XBee();

// Buffer for LX7007 data
#define BUFFLEN 100
char lxBuffer[BUFFLEN];
char* lxBuffNext;

void setup()
{
  // Serial setup for xBee communication
  mySerial.begin(9600);
  while (!mySerial) continue;

  // xBee API setup
  xbee.setSerial(mySerial);

  // Serial setup for LX7007 communication
  lxSerial.begin(19200);
  Serial.begin(19200);
  while (!lxSerial) continue;

  // Initialize buffer pointer:
  lxBuffNext = lxBuffer;
}


void sendData(int ias, int height)
{
  // Construct json by hand
  String json = String( "{\"IAS\":" + String(ias) + ",\"HEI\":" + String(height) + "}" );

  uint8_t payload[json.length() + 1]; //The +1 is there because the string is null terminated 
  json.toCharArray(payload, json.length() + 1); 

  // Send data
  
  XBeeAddress64 addr64 = XBeeAddress64(DEST_LOW, DEST_HI);
  ZBTxRequest zbTx = ZBTxRequest(addr64, payload, json.length());
  xbee.send(zbTx);
  return;
}

void processBuffer(float* ias, float* height)
{  
  String buff = String(lxBuffer);   // Convert to String for easier pharsing
  
  if ( !buff.startsWith("LXWP0") )  // Check if valid NMEA frame
  {
    *ias = *height = -1;
    return;
  }

  int iasStart = 8;
  int iasEnd = buff.indexOf(',', iasStart);
  int heightEnd = buff.indexOf(',', iasEnd + 1);

  *ias = buff.substring(iasStart, iasEnd).toFloat();
  *height = buff.substring(iasEnd + 1, heightEnd).toFloat();
  return;
}

void loop() 
{
  float ias, height;
  int incomingByte;
  
  if (lxSerial.available() > 0)
   {
     incomingByte = lxSerial.read();    // Get next byte from serial and write it in the buffer
     //Serial.write(incomingByte);
    
     if (incomingByte == '$')         // If new frame starts, process last frame, reset buffer and send data
     {
        lxBuffNext = '\0';            // Null terminate buffer
        processBuffer(&ias, &height);  // Extract data
        lxBuffNext = lxBuffer;         // Reset buffer

        if ( ias > 0 && height > 0 )  // If data is valid, send it.
           sendData(ias, height);     

        //Serial.print(ias);
        //Serial.print("\n");
        //Serial.print(height);
        //Serial.print("\n");
     }
     else
     {
        *lxBuffNext = incomingByte;
        lxBuffNext += 1;                // Move buffer pointer
        
        if (lxBuffNext - lxBuffer > BUFFLEN) // avoid buffer overflow
           lxBuffNext = lxBuffer;
     }
   }
}
