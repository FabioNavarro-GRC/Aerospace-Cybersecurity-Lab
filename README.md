# Aerospace Cybersecurity Lab

## Overview
This repository documents a research project focused on **embedded systems security and aerospace communications**. The primary goal is to design, construct, and audit a **FlatSat** (a satellite bus deployed on a test bench) to analyze vulnerabilities in low-power telemetry links and develop robust security countermeasures.


## System Architecture
The system simulates a distributed satellite environment:
- **Space Segment (Payload):** Arduino Nano, DHT22 sensor (telemetry), and HC-12 transceiver.
- **Ground Segment:** Raspberry Pi 4 acting as the On-Board Computer (OBC) and primary transceiver.
- **Auditing Tools:** RTL-SDR v4 and HackRF One for RF spectrum analysis and traffic sniffing.

## Security Implementation
To ensure the integrity and confidentiality of the telemetry data, this project implements AES-128 (ECB Mode) symmetric encryption:
End-to-End Encryption: Data is encrypted on the source before transmission and decrypted at the destination.
Obfuscation: Base64 encoding is utilized to protect the encrypted binary payload during transit.
Credential Management: Sensitive API keys are isolated in a local config.py file, excluded from version control to prevent leaks.

## Learning Roadmap
- [X] **Phase 1: Hardware Integration.** Assembly, soldering, and configuration of the FlatSat nodes.
- [X] **Phase 2: Telemetry Link.** Implementation of UART serial protocols for robust data transmission.
- [ ] **Phase 3: RF Auditing.** Signal analysis in the 433MHz band using SDR to detect information leakage.
- [ ] **Phase 4: Resilience & Defense.** Investigation of common attacks (Jamming, Spoofing) and development of lightweight encryption/authentication mechanisms.

## Repository Structure
```text
├── /docs          # Technical reports, schematics, and research notes.
├── /src           # Source code (C++ for Arduino, Python for Raspberry Pi).
├── /images        # Flowcharts, wiring diagrams, and setup photography.
└── README.md      # Main documentation.

## Tech Stack
-Hardware: Raspberry Pi 4, Arduino Nano, HC-12 (433MHz), RTL-SDR v4, HackRF One.
-Software: Python 3, C++ (Arduino IDE), GNU Radio, SDR++.

## Research Objectives
-Analyze inherent vulnerabilities of unencrypted, non-authenticated telemetry protocols.
-Implement security techniques tailored for resource-constrained embedded systems.
-Contribute to the aerospace cybersecurity knowledge base within the Polish aerospace ecosystem.

**Project currently in development as part of a professional training path in Aerospace Cybersecurity.**

**For detailed technical documentation and lab setup, see the /docs directory.**
