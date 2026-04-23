# 🩺 EquiCare AI: Diagnostic De-Biasing Engine

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.33.0-FF4B4B.svg?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/AI_Engine-Google_Gemini_Flash--Lite-blueviolet.svg?logo=google)
![JSON](https://img.shields.io/badge/Data-JSON-lightgrey.svg)
![Solution Challenge](https://img.shields.io/badge/Hack2Skill-Solution_Challenge_2026-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**[🔴 View Live Demo Here](https://your-live-url-goes-here.com)** *(Note: Replace with your actual Streamlit Community Cloud link)*

> **Securing equitable healthcare through intelligent, real-time algorithmic auditing.**

EquiCare AI operates as a robust algorithmic governance middleware designed to detect, audit, and mitigate demographic bias in predictive healthcare models. It forces transparency by intercepting black-box diagnostic algorithms and utilizing Large Language Model (LLM) orchestration to ensure medical decisions are equitable and free from historical data skews.

---

## 🚀 See It In Action

### The AI Governance Engine Under the Hood
*Our Streamlit dashboard seamlessly transitioning between proactive data auditing and reactive patient diagnostics.*
![EquiCare AI Live Dashboard](Equicare07%20GIF.gif)

---

## 🛑 The Problem: "Invisible Algorithmic Harm"
Predictive medical AI models often carry fatal demographic biases inherited from historical training data, leading to a massive crisis in clinical equity.
* 📉 **Demographic Skew:** Datasets are heavily weighted toward specific demographics (e.g., relying on male physiological data for cardiac events).
* 👻 **Atypical Erasure:** Black-box algorithms frequently misdiagnose or ignore atypical symptoms in underrepresented groups.
* 🔇 **Algorithmic Gaslighting:** Patients receive inaccurate "Low Risk" scores, leading to wrongful discharges and severe clinical harm.

## 💡 The Solution: Dual-Phase AI Governance
EquiCare AI replaces opaque algorithmic guessing with an **Automated Governance Loop**:
1. **Pre-Model Audit 📊:** Hospital admins input proposed training dataset parameters. The AI flags inherent demographic skews *before* training begins.
2. **Clinical Interception 🩺:** A physician inputs live patient data. If the hospital's black-box model outputs a suspicious score, the middleware intercepts it.
3. **AI Trace 🧠:** Google Gemini orchestrates a retrospective explainability trace, analyzing the clinical context against the flawed algorithm.
4. **Correct & Notify 📲:** The system generates a human-readable fairness report, explaining the algorithmic failure and providing a bias-corrected medical recommendation.

---

## ✨ Key Features
* 🔍 **Proactive Data Auditing:** Detects feature bias risks and underrepresented cohorts in raw historical datasets.
* 🛡️ **Reactive Explainability Tracing:** Real-time interception of black-box diagnostic outputs for instantaneous bias auditing.
* 🔄 **LLM Orchestration:** Powered by Google Gemini Flash-Lite to handle complex JSON data structuring and semantic medical reasoning with extreme low-latency.
* 📋 **Automated Markdown Reporting:** Generates structured, professional Fairness Audit Reports directly for attending physicians.

---

## 📸 System Previews

### 1. Phase 1: Pre-Model Data Auditing
*Administrators input historical clinical dataset parameters for pre-training evaluation.*
![Pre-Model Data Audit Initialization](Screenshot%202026-04-24%20005016.png)

*The LLM orchestrates a deep-dive analysis, flagging intersectional blindness and outputting actionable data-rebalancing techniques.*
![Phase 1: Generative Bias Assessment Report](Screenshot%202026-04-24%20005049.png)
![Strategic Mitigation Protocols](Screenshot%202026-04-24%20005324.png)

### 2. Phase 2: Post-Model Explainability Tracing
*The middleware flags a potentially lethal "Low Risk" discharge order due to missing fairness metrics.*
![Phase 2: Black-Box Interception & Patient Context](Screenshot%202026-04-24%20005337.png)

*Gemini Flash-Lite generates a real-time audit, explaining the algorithmic failure and providing a bias-corrected clinical recommendation.*
![Phase 2: Retrospective Explainability Trace](Screenshot%202026-04-24%20005409.png)

---

## 🛠️ Technology Stack
* **Frontend & UI Rendering:** `Streamlit` (Python)
* **AI/Machine Learning:** `Google Gemini Flash-Lite API` (via Google AI Studio)
* **Data Structuring:** `Python` Dictionaries, `JSON`
* **Cloud Infrastructure:** `Streamlit Community Cloud`

---

## 💻 Quick Start Guide (Local Deployment)

### Prerequisites
* Python 3.9+
* Git
* Google AI Studio API Key

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/symbiote07/equicare-ai-governance.git
   cd equicare-ai-governance
   ```
   
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Secrets:**
    *Create a hidden Streamlit secrets directory to secure your Gemini API key.*
    ```bash
    mkdir .streamlit
    # On Windows use: type NUL > .streamlit\secrets.toml
    touch .streamlit/secrets.toml
    ```
    *Open `secrets.toml` and add your key:*
    ```toml
    GEMINI_API_KEY = "your_api_key_here"
    ```

4.  **Launch the Streamlit Dashboard:**
    ```bash
    streamlit run app.py
    ```
    *The dashboard will automatically open in your default web browser.*

---

## 🤝 Open for Collaboration

This project is open-source and actively seeking contributors! Areas where we'd love your help:

  * 🏥 **EHR Integration:** Building pipelines to integrate directly with hospital Electronic Health Records (EHR) via FHIR/HL7 protocols.
  * 🧠 **Specialized Model Swapping:** Creating configuration files to easily swap from Gemini Flash-Lite to enterprise Vertex AI Pro models for production-grade clinical reasoning.
  * 🌍 **Multi-lingual Output:** Utilizing LLM translation capabilities to generate audit reports for international medical teams.

Feel free to **Fork** the repository and submit a **Pull Request**!

---

<p align="center">
<i>Developed by <b>Aryan Shukla (Team pennywise07)</b> for robust, transparent, and equitable healthcare diagnostics.</i>
</p>
