
/* 
 * File:   sensor_node.ino
 * Author: Jan Molina
 * 
 * Description:
 * 
 *   Code that executes on a sensor node.
 *   
 * Data transmission format:
 * 
 *   IDENTITY,VALUE
 * 
 * Created on November 17, 2023, 8:25 PM
 */
#define BUFLEN  64

String identity1 = "ROOM_600";  // hard-coded sensor identity
String identity2 = "ROOM_999";
char outbuf[BUFLEN];
int  anval = 0;
int counter = 0;

void setup() 
{
  Serial.begin(9600);
}

void sensor_transmit(String identity, double value)
{
  // Send the data out to the Xbee
  Serial.print(identity + ",");
  Serial.print(value);
  Serial.print("\n");
}

void loop() 
{
  anval = analogRead(A0);  // Read something from a sensor
  double val1 = anval;
  double val2 = anval * 5;
  if ((counter % 2) == 0) {
    sensor_transmit(identity1, val1);
  } else {
    sensor_transmit(identity2, val2);
  }

  delay(1000);

  counter++;
}
