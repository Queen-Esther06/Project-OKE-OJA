# Project Oke-Oja (The Sovereign Trust Protocol)

## Overview

Project Oke-Oja is a decentralized, offline-first trade settlement and identity verification protocol engineered to protect open-air market traders, roadside wholesalers, and informal suppliers from capital flight, physical phone theft, and inventory fraud. By eliminating the overt-dependence on continuous internet connectivity, Oke-Oja guarantees transaction execution within high-density, low-infrastructure commerce zones.

The architecture multi-stitches three foundational themes:

* **Digital Tools for SMEs & Informal Sector**
* **Cybersecurity & Data Protection**
* **Fintech & Digital Payments**

---

## Technical Architecture & Mechanics

The protocol handles trade processing across a multi-layered offline infrastructure to maintain seamless, network-independent transaction finality:

1. **Identity Handshake (NFC):** Initiates a rapid, offline Near Field Communication touch to securely exchange merchant configuration and routing details.
2. **Primary Data Channel (AcousticDT):** Modulates the transaction payload into encrypted sound waves transmitted device-to-device via standard microphones and speakers.
3. **Redundancy Layer (BLE Mesh):** Fallback mechanism that automatically routes payload data via a local Bluetooth Low Energy Mesh network if high ambient market noise interrupts the acoustic channel.
4. **Deferred Settlement:** Stores signed ledger states within the device's localized secure cryptographic enclave, batch-syncing to the OPay central core only during a cellular resumption event.

<img width="722" height="414" alt="Runtime implementation flowchart" src="https://github.com/user-attachments/assets/8f37ef6e-b611-41b8-be1f-0ccea962fb03" />

---

## Telemetry Biometrics Engine

To neutralize physical security risks and coerced security actions, Oke-Oja deploys continuous background validation:

* **Ambient Metrics:** Tracks hardware data streams to profile user walking gait, typing cadence, and grip pressure.
* **System-Wide Asset Freeze:** Detects anomalous physical behavior or sudden device snatches to trigger an immediate asset lock.
* **Social Recovery Ring:** Requires a physical cryptographic confirmation signature from a designated peer merchant's node to unlock the terminal, rendering forced PIN disclosures useless.

---

## Repository Layout

```text
├── .github/workflows/      # CI/CD automated deployment pipelines
├── Acoustics/            # Audio DSP, FSK modulation, and demodulation modules
├── BLE-mesh/               # Localized BLE peer node discovery and packet routing
├── Telemetry-engine/       # On-device ML models tracking gait, grip, and typing cadence
├── NFC-handshake/          # Offline card emulation and proximity exchange scripts
├── Core-enclave/           # Hardware ledger caching and multi-sig peer validation
└── Dashboard-shell/        # Interactive interface prototype shell for presentation

```

---

## Sandbox Testing & Simulation

Development execution is structured around isolated verification sandboxes:

### 1. Acoustic Sandbox (`/Acoustics`)

Evaluates multi-frequency Frequency Shift Keying (FSK) sound modulation. Sandbox utilities enable engineering teams to verify acoustic packet transfer integrity against simulated, high-noise marketplace sound files.

### 2. BLE Mesh Simulation (`/BLE-mesh`)

Manages localized peer node provisioning, latency logging, and background failover switching configurations without relying on active cloud networks.

### 3. Telemetry Profiling (`/Telemetry-engine`)

Ingests native accelerometer, gyroscope, and touchscreen data streams to train low-footprint, on-device machine learning models for user identity baselines.

---

## Setup & Deployment

### Prerequisites

* Native mobile development environment supporting low-level audio pipelines, BLE peripheral control, and hardware secure storage access.
* Target devices equipped with functional microphones, speakers, and standard NFC modules.

### Quick Start

1. Clone the repository:
```bash

```



git clone https://github.com/Queen-Esther06/Project-OKE-OJA.git
cd Project-OKE-OJA

```
2. Run isolated trial tests for the acoustic data transfer component:
   ```bash
cd "Prototype & Testing\Acoustics" && python tests\run_manual_test.py

```

3. Initialize the telemetry data capture baseline compilation:
```bash

```





```

```
