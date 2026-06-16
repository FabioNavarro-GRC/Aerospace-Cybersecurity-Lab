# Threat Modeling: Aerospace-Cybersecurity-Lab (FlatSat)

## 1. Scope
This document analyzes the vulnerabilities of the point-to-point telemetry link between the Space Segment (Arduino + HC-12) and the Ground Segment (Raspberry Pi + HC-12).

## 2. Data Flow Diagram
[Sensor DHT22] -> [Arduino] --(RF 433MHz)--> [Raspberry Pi] -> [Log File]

## 3. Threat Matrix (STRIDE Model)

| Threat | Category | Description | Impact |
| :--- | :--- | :--- | :--- |
| **Spoofing** | Identity | An attacker sends fake data masquerading as the Arduino. | High (Erroneous decisions) |
| **Tampering** | Integrity | Modification of data packets during transmission. | Medium (Corrupted data) |
| **Replay** | Authenticity | Intercepting a valid packet and retransmitting it later. | Medium (Log confusion) |
| **Jamming** | Availability | Saturating the 433MHz frequency to cut telemetry. | Critical (Link loss) |
| **Eavesdropping** | Confidentiality | Intercepting and reading unencrypted telemetry. | Low (Non-critical data) |

## 4. Planned Mitigations
- [ ] **Phase 2:** Implement basic checksums to detect data corruption.
- [ ] **Phase 3:** Spectrum analysis to identify Jamming patterns.
- [ ] **Phase 4:** Development of an authentication protocol (HMAC) to prevent Spoofing.
