---
layout: default
title: Projects
---

---
layout: default
title: Projects
---

# 🛡️ The Sentinel Hybrid-SOC
### Automated Detection & Response Ecosystem for Hybrid-Cloud Environments
**Author:** Yessy Vasquez | DAE Cybersecurity Cohort — Stafford, CT | 2026

---

## What This Project Is

The Sentinel Hybrid-SOC is a fully operational Security Operations Center (SOC) built inside a virtualized lab environment. I designed and built this system to solve a real-world security problem: most entry-level security setups only watch local networks — they miss cloud-based attacks and have no automated way to respond.

This project integrates on-premise endpoint monitoring with AWS cloud detection, all feeding into a single Wazuh SIEM dashboard. I then simulated real attacker techniques against my own infrastructure and documented every detection.

**The result:** A live detection system that caught two real attack simulations — an SSH brute force and a cloud credential theft — and generated professional incident reports for both.

---

## Tech Stack

| Category | Tool / Platform |
|---|---|
| SIEM / EDR | Wazuh v4.14.4 (Docker, single-node) |
| Virtualization | UTM (Apple Silicon), Kali Linux ARM64 |
| Cloud | AWS CloudTrail, S3, IAM, Secrets Manager |
| Attack Simulation | Kali Linux, Atomic Red Team |
| SOAR (Phase 3) | Shuffle (in progress) |
| Framework | MITRE ATT&CK |
| Hardware | Apple Mac M4 |

---

## Project Phases

### ✅ Phase 1 — "The Bones" (Infrastructure)
Built the core detection infrastructure from scratch:
- Deployed Wazuh Manager via Docker on Mac M4 (IP: 10.11.3.152)
- Provisioned Kali Linux ARM64 in UTM as a monitored endpoint (Agent ID: 001, IP: 10.11.3.106)
- Confirmed agent-manager communication — KALI-UTM showing **Active** in Wazuh dashboard
- Configured AWS CloudTrail trail (`sentinel-soc-trail`) with multi-region logging
- Connected CloudTrail → S3 → Wazuh aws-s3 wodle for cloud log ingestion

### ✅ Phase 2 — "The Nerves" (Attack Simulation & Detection)
Simulated two real-world attack scenarios and detected both:

**Attack 1 — SSH Brute Force** (April 21, 2026)
- Simulated repeated failed SSH login attempts against KALI-UTM
- Wazuh fired **Rule 5712** (Level 10 — HIGH severity)
- 28 authentication failures recorded, 0 successful logins
- MITRE ATT&CK: `T1110 — Brute Force` | Tactic: `TA0006 Credential Access`
- Compliance: PCI DSS 11.4, HIPAA 164.312.b, NIST 800-53 SI.4

**Attack 2 — Cloud Credential Theft** (May 4, 2026)
- Used stolen IAM credentials to make 10 rapid GetSecretValue calls to AWS Secrets Manager
- All 10 calls were denied at the IAM permission level — zero secrets accessed
- Wazuh fired **Rule 80250** (AWS AccessDenied) within 5 minutes via CloudTrail ingestion
- MITRE ATT&CK: `T1526 Cloud Service Discovery` | `T1528 Steal Application Access Token`
- Tactics: `TA0001 Initial Access`, `TA0006 Credential Access`, `TA0007 Discovery`

### 🔄 Phase 3 — "The Brain" (SOAR Automation) — In Progress
- Integrating Shuffle SOAR to automate containment workflows
- Goal: automated host isolation triggered by Wazuh alerts, reducing Mean Time to Respond (MTTR)

---

## Detections Summary

| Incident | MITRE Technique | Wazuh Rule | Severity | Outcome |
|---|---|---|---|---|
| SSH Brute Force | T1110 — Brute Force | Rule 5712 | Level 10 (HIGH) | 28 failures, 0 breaches |
| Cloud Credential Theft | T1526, T1528 | Rule 80250 | Level 5 | 10 API calls blocked, 0 secrets stolen |

---

## Key Skills Demonstrated

- **Threat Detection** — Real-time alerting using behavioral rules, not signatures
- **MITRE ATT&CK Mapping** — Every attack technique documented to the framework
- **Cloud Security** — AWS CloudTrail integration, IAM policy analysis, S3 log pipeline
- **Incident Response** — NIST SP 800-61 process applied to each incident
- **SIEM Administration** — Wazuh configuration, agent management, rule tuning
- **Documentation** — Professional incident reports generated for every high-severity alert

---

## Compliance Frameworks Covered

PCI DSS · HIPAA · NIST SP 800-53 · NIST SP 800-61

---

## About Me

I'm an aspiring Incident Response Analyst building hands-on SOC skills through a live, hybrid-cloud detection lab. Every detection in this project came from a real simulation I ran against infrastructure I built myself.

📄 [View My Resume](./Yessy-Vasquez-Cyber-Security-Researcher.pdf) | 💼 [LinkedIn](https://www.linkedin.com/in/yessyvasquez)