# Quantum Cryptography: BB84 Security Analysis Toolkit

A Python toolkit and research repository for analyzing the security of the BB84 Quantum Key Distribution (QKD) protocol under various eavesdropping strategies and noise conditions.

The project combines reusable Python modules, simulation utilities, visualization tools, and Jupyter notebooks to study the impact of adversarial attacks on secure quantum communication.

---

## Overview

BB84 is the first and most widely studied Quantum Key Distribution protocol. Its security relies on fundamental quantum mechanical principles, including:

* Quantum Superposition
* Measurement Disturbance
* Basis Incompatibility
* No-Cloning Theorem

This repository provides implementations for:

* BB84 Protocol Simulation
* Intercept-Resend Attacks
* Random Basis Attacks
* Noise-Aware Communication Channels
* Quantum Bit Error Rate (QBER) Analysis
* Security Visualization and Evaluation

---

## Security Analysis Workflow

```bash
Alice Generates Random Bits
            ↓
BB84 State Encoding
            ↓
Quantum Transmission
            ↓
(Optional) Eve Intercepts
            ↓
Bob Measures Qubits
            ↓
Basis Reconciliation
            ↓
Key Sifting
            ↓
QBER Calculation
            ↓
Attack Detection
            ↓
Secure Key Generation
```

---

## Repository Structure

```text
Quantum-Cryptography-BB84-Security-Analysis/
│
├── setup.py
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── 01_BB84_Eavesdropping_Attacks_Classical_Simulation.ipynb
│   ├── 02_BB84_Eavesdropping_Attacks_Qiskit.ipynb
│   └── 03_BB84_Eavesdropping_Attacks_and_Noise_Analysis.ipynb
│
├── examples/
│   ├── baseline_bb84.py
│   ├── intercept_resend_demo.py
│   └── noise_analysis_demo.py
│
└── src/
    └── bb84_security/
        │
        ├── __init__.py
        ├── protocol.py
        ├── attacks.py
        ├── noise.py
        ├── analysis.py
        └── visualization.py
```

---

## Features

### BB84 Protocol Simulation

Simulate secure key exchange between Alice and Bob using randomly generated bits and measurement bases.

Features:

* Random Bit Generation
* Random Basis Selection
* Key Sifting
* Secure Key Extraction
* QBER Computation

---

### Eavesdropping Attacks

Study the effect of adversarial behavior on communication security.

Implemented Attacks:

#### Intercept-Resend Attack

Eve measures transmitted qubits and resends reconstructed states.

#### Random Basis Attack

Eve performs probabilistic measurements using randomly chosen bases.

#### Extensible Attack Framework

New attack models can easily be added through the attack interface.

---

### Noise Modeling

Investigate realistic quantum communication channels.

Supported Models:

* Depolarizing Noise
* Channel Errors
* Measurement Errors

---

### Security Metrics

Evaluate protocol robustness using:

* Quantum Bit Error Rate (QBER)
* Information Leakage
* Key Agreement Accuracy
* Detection Probability

---

### Visualization Tools

Generate plots for:

* QBER vs Attack Probability
* QBER vs Noise Strength
* Security Comparisons
* Protocol Performance Metrics

---

## Mini Project: Security Evaluation of the BB84 Quantum Key Distribution Protocol

### Objective

The objective of this project was to investigate the security of the BB84 Quantum Key Distribution (QKD) protocol under multiple eavesdropping strategies and communication environments.

The study evaluates how different attack models influence the Quantum Bit Error Rate (QBER), information leakage, and the ability of Alice and Bob to detect malicious interception.

---

### Methodology

The project was divided into three stages:

#### Stage 1: Classical Simulation

A classical BB84 simulator was implemented to establish baseline protocol behavior and evaluate the impact of several eavesdropping strategies:

* Intercept-Resend Attack
* Random Basis Attack
* Entanglement-Based Attack
* Photon Number Splitting (PNS) Attack

Performance metrics such as QBER and key agreement rates were measured under varying attack probabilities.

---

#### Stage 2: Quantum Simulation using Qiskit

The BB84 protocol was recreated using Qiskit quantum circuits and executed on ideal quantum simulators.

The study analyzed:

* Quantum state preparation
* Basis encoding and measurement
* Attack-induced disturbances
* Security detection thresholds

This stage validated the classical results using quantum circuit implementations.

---

#### Stage 3: Noise-Aware Security Analysis

Realistic communication channels were introduced through quantum noise models.

The investigation explored:

* Depolarizing noise
* Channel imperfections
* Noise-induced QBER
* Distinguishing attacks from natural channel errors

This provided a more practical assessment of BB84 security in real-world quantum communication systems.

---

### Key Findings

#### Baseline BB84 Performance

Under ideal conditions without an eavesdropper, the protocol achieved negligible QBER and successful key agreement between Alice and Bob.

---

#### Impact of Eavesdropping

Intercept-resend attacks produced significant increases in QBER, making the presence of an attacker detectable through basis reconciliation and error analysis.

As attack probability increased:

* QBER increased
* Key quality decreased
* Eve's information gain increased

This demonstrated the fundamental security mechanism of BB84.

---

#### Noise vs. Adversarial Activity

The noisy-channel simulations revealed that both channel imperfections and eavesdropping introduce errors into the shared key.

The analysis highlights the importance of selecting appropriate QBER thresholds to distinguish legitimate channel noise from active attacks.

---

### Outcome

The project demonstrates how quantum mechanical principles provide intrinsic security guarantees that are impossible in classical cryptographic key exchange.

Through classical simulations, Qiskit-based quantum implementations, and noise-aware evaluations, the study illustrates how BB84 can detect eavesdropping attempts and maintain secure communication under realistic operating conditions.


---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Quantum-Cryptography-BB84-Security-Analysis.git

cd Quantum-Cryptography-BB84-Security-Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the package locally:

```bash
pip install -e .
```

---

## Quick Start

### Baseline BB84 Simulation

```python
from bb84_security import BB84Protocol

protocol = BB84Protocol(
    num_bits=1000
)

results = protocol.run()

print(results["qber"])
```

---

### Intercept-Resend Attack

```python
from bb84_security.protocol import BB84Protocol
from bb84_security.attacks import InterceptResendAttack

protocol = BB84Protocol(
    num_bits=1000
)

protocol.generate_data()

attack = InterceptResendAttack()

protocol.bob_bits = attack.apply(
    protocol.alice_bits,
    protocol.alice_bases,
    protocol.bob_bases
)

print(
    protocol.compute_qber()
)
```

---

## Example Scripts

Run included demonstrations:

### Baseline Protocol

```bash
python examples/baseline_bb84.py
```

### Intercept-Resend Attack

```bash
python examples/intercept_resend_demo.py
```

### Noise Analysis

```bash
python examples/noise_analysis_demo.py
```

---

## Technologies Used

### Quantum Computing

* Qiskit
* Qiskit Aer
* IBM Quantum Runtime

### Scientific Computing

* NumPy
* SciPy

### Visualization

* Matplotlib

### Development Environment

* Python
* Jupyter Notebook

---

## Skills Demonstrated

This project demonstrates practical experience in:

* Quantum Cryptography
* Quantum Key Distribution
* BB84 Protocol Design
* Quantum Security Analysis
* Qiskit Development
* Noise Modeling
* Scientific Python Development
* Software Packaging
* Data Visualization

---

## Applications

The techniques explored in this repository are relevant to:

* Secure Communications
* Quantum Networking
* Quantum Internet Research
* Post-Quantum Security
* Cybersecurity Research
* Quantum Information Science

---

## Future Improvements

Potential future additions include:

* Entanglement-Based Attacks
* Photon Number Splitting (PNS) Attacks
* B92 Protocol Support
* E91 Protocol Support
* Device-Independent QKD
* IBM Quantum Hardware Experiments
* Statistical Security Analysis
* Quantum Network Simulations

---

## Author

**Shriram**

Areas of Interest:

* Quantum Computing
* Quantum Cryptography
* Quantum Machine Learning
* Quantum Optimization
* Artificial Intelligence

GitHub: https://github.com/Shr-i-ram

---

## License

This repository is intended for educational and research purposes.
