
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

char *identity = "SENS001";  // hard-coded sensor identity
char outbuf[BUFLEN];
int  value = 0;

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  value = analogRead(A0);  // Read something from a sensor
  
  snprintf(outbuf,BUFLEN,"%s,%d\n",
    identity,
    value);
  Serial.print(outbuf);    // Send it out to xbee via serial
  
  delay(1000);

}
