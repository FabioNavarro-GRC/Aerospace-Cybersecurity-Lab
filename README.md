# Aerospace Cybersecurity Lab

## Overview
This repository documents a research project focused on **embedded systems security and aerospace communications**. The primary goal is to design, construct, and audit a **FlatSat** (a satellite bus deployed on a test bench) to analyze vulnerabilities in low-power telemetry links and develop robust security countermeasures.



## System Architecture
The system simulates a distributed satellite environment:
- **Space Segment (Payload):** Arduino Nano, DHT22 sensor (telemetry), and HC-12 transceiver.
- **Ground Segment:** Raspberry Pi 4 acting as the On-Board Computer (OBC) and primary transceiver.
- **Auditing Tools:** RTL-SDR v4 and HackRF One for RF spectrum analysis and traffic sniffing.

## Learning Roadmap
- [ ] **Phase 1: Hardware Integration.** Assembly, soldering, and configuration of the FlatSat nodes.
- [ ] **Phase 2: Telemetry Link.** Implementation of UART serial protocols for robust data transmission.
- [ ] **Phase 3: RF Auditing.** Signal analysis in the 433MHz band using SDR to detect information leakage.
- [ ] **Phase 4: Resilience & Defense.** Investigation of common attacks (Jamming, Spoofing) and development of lightweight encryption/authentication mechanisms.

## Repository Structure
```text
├── /docs          # Technical reports, schematics, and research notes.
├── /src           # Source code (C++ for Arduino, Python for Raspberry Pi).
├── /images        # Flowcharts, wiring diagrams, and setup photography.
└── README.md      # Main documentation.
