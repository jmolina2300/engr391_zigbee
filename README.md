## ZigbeeNet

  
Simple Zigbee sensor network to be implemented with Xbee S2C RF modules.

**Components**
- (2x) Xbee S2C RF modules
- (2x) Xbee USB adapter boards
- (1x) Raspberry Pi (or laptop)
- (1x) Arduino Nano (or any microcontroller)
- (1x) breadboard

**Software**
- XCTU - to configure the Xbee modules

**Python Requirements**
- pyserial
- matplotlib

## Usage  
#### Base station
The "data_collector" script is run from the Raspberry Pi or whatever device is used as the base station. This script listens on a specified serial device and writes the data to a CSV file. For example,
`./data_collector.py /dev/ttyUSB0`

Once that script is running and capturing data, you can start up the displayer script with an argument for the CSV file to display. For example,
`./displayer.py SENSORNAME.csv`

#### Sensor Nodes
The "sensor_node" arduino sketch is uploaded to whatever microcontroller you use.  You must set the desired name/identity of the sensor from within this sketch. The base station will receive the data being sent by this sensor and use the identity supplied to create a CSV file for it.



## Xbee Module configuration    
This section describes the fields which will need to be configured In the XCTU software for each Xbee module. You must configure each Xbee module to play the necessary Zigbee device role in order for the network to operate. In particular, the base station must be the Coordinator, and the sensor nodes must be either Routers, or Zigbee End devices. 

The following is an example, in table format, of the fields that must be altered to differentiate the two nodes. **Note** that the PAN ID value is the same for both; this is necessary to ensure that the devices are part of the same network and can communicate with one another.


| Field | Base Station | Sensor Node |
|--|--|--|
| PAN ID | 123F | 123F |
| CE | 1 | 0 |
| DH| 0000 | 0000 |
| DL| FFFF | 0000 |
| JV| 0| 1 |
