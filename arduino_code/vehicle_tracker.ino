#include <TinyGPS++.h>
#include <HardwareSerial.h>

TinyGPSPlus gps;

HardwareSerial gpsSerial(2);

void setup()
{
  Serial.begin(115200);

  gpsSerial.begin(
      9600,
      SERIAL_8N1,
      16,
      17);
}

void loop()
{
  while(gpsSerial.available())
  {
    gps.encode(gpsSerial.read());

    if(gps.location.isUpdated())
    {
      float lat =
          gps.location.lat();

      float lon =
          gps.location.lng();

      Serial.print("Lat:");
      Serial.println(lat);

      Serial.print("Lon:");
      Serial.println(lon);
    }
  }
}