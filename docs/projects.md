---
layout: default
title: Projects
---

# 🛡️ The Sentinel Hybrid-SOC 
 
![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square) ![SIEM: Wazuh](https://img.shields.io/badge/SIEM-Wazuh-blue?style=flat-square&logo=wazuh) ![Cloud: AWS](https://img.shields.io/badge/Cloud-AWS-orange?style=flat-square&logo=amazonaws) ![SOAR: Shuffle](https://img.shields.io/badge/SOAR-Shuffle-purple?style=flat-square) ![Framework: MITRE ATT&CK](https://img.shields.io/badge/Framework-MITRE%20ATT%26CK-red?style=flat-square) ![Platform: Mac M4 ARM64](https://img.shields.io/badge/Platform-Mac%20M4%20ARM64-black?style=flat-square&logo=apple) 
 
> A fully functional Security Operations Center (SOC) built from scratch — 
> combining on-premise endpoint detection with cloud security monitoring 
> and automated incident response. 
 
--- 
 
## 📌 About This Project 
 
The Sentinel Hybrid-SOC is a hands-on cybersecurity capstone project that 
simulates a real-world enterprise SOC environment. Built entirely in a 
virtualized home lab, it integrates industry-standard open-source tools to 
detect, analyze, and automatically respond to multi-stage cyberattacks across 
both local endpoints and AWS cloud infrastructure. 
 
This project goes beyond theory — every component was deployed, configured, 
and tested against live attack simulations mapped to the MITRE ATT&CK framework. 
 
--- 
 
## ⚙️ Tech Stack 
 
| Layer | Tool | 
|---|---| 
| SIEM / EDR | Wazuh v4.x (Docker) | 
| Attack Simulation | Atomic Red Team (Linux) | 
| Cloud Security | AWS CloudTrail + GuardDuty | 
| SOAR / Automation | Shuffle | 
| Virtualization | UTM (Mac M4 ARM64) + Kali Linux | 
| Framework | MITRE ATT&CK | 
 
--- 
 
## 🔍 What It Does 
 
- **Detects** endpoint threats in real time using Wazuh File Integrity 
  Monitoring and behavioral rules 
- **Monitors cloud activity** by ingesting AWS CloudTrail logs into Wazuh 
  via S3 polling — catching credential theft and unauthorized API calls 
- **Simulates real attacks** using Atomic Red Team (file modification, 
  SSH brute force, cloud credential abuse) 
- **Automates response** with Shuffle SOAR workflows that trigger 
  containment actions when high-severity alerts fire 
- **Maps every detection** to MITRE ATT&CK tactics and techniques 
  for professional-grade threat documentation 
 
--- 
 
## 🏗️ Architecture