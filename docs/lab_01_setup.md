# Lab 01: Hardware Setup

## Objective
Establish the communication link for the FlatSat.

## Status
- [X] Soldering HC-12 pins.
- [X] Configuring Arduino Nano.
- [X] Establishing UART link.

## Hardware Configuration

| Component | Function | Connection Details |
| :--- | :--- | :--- |
| **Arduino Nano** | Controller | DHT22 (Pin 4), HC-12 (SoftwareSerial 2,3) |
| **DHT22** | Sensor | VCC: 5V, GND, Data: Pin 4 |
| **HC-12** | Radio Transceiver | TX/RX to Arduino, SET pin disconnected |

![Hardware Setup del FlatSat](images/hardware_configuration.jpg)

## Communication Parameters
To ensure reliable data transmission, the system operates under the following UART configuration:

* **Baud Rate:** 9600 bps
* **Mode:** Transparent Transmission (Transparent Mode)
* **Frequency:** Channel 20 (Optimized via RF Audit)

## Telemetry Format
Data is transmitted using a comma-separated key-value protocol for parsing:
`H:<humidity>,T:<temperature>`

> **Example:** `H:45.2,T:22.1`

## Verification
The system was verified by monitoring the Serial output on the Arduino IDE and successfully capturing the data stream on the Raspberry Pi ground station.

*Note: Optimized RF parameters were established in the subsequent RF Auditing lab, moving the link from default settings to Channel 20 to mitigate local interference.*
