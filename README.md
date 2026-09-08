#  HealthHive

## AI-Powered Safety Intelligence Platform for SIF Precursor Detection

HealthHive is an **AI/NLP-powered workplace safety intelligence platform** designed to analyze **Unsafe-Act, Unsafe-Condition, and Near-Miss reports** and identify potential **Serious Injury and Fatality (SIF) precursors**.

The platform converts unstructured safety observations into structured, prioritized safety insights, helping **HSE teams identify critical risks, review uncertain cases, track corrective actions, and take preventive action before serious incidents occur.**

Website Link - file:///C:/Users/Haripriya/.codex/.chatgpt-projects/g-p-6aa00ce0fb10819196866a8a8f05807f/index.html
---

## 🎯 Problem Statement

### AI/NLP Engine to Detect Serious Injury & Fatality (SIF) Precursors in OIL's Safety Reports

Oil India Limited (OIL) receives a large volume of:

* Unsafe-Act Reports
* Unsafe-Condition Reports
* Near-Miss Reports

Manually analyzing these reports makes it difficult to quickly identify **SIF-potential situations, recurring safety patterns, and high-risk conditions**.

HealthHive addresses this challenge by using AI/NLP to automatically analyze reports, classify their SIF potential, map them to relevant safety rules, and prioritize risks for HSE teams.

---

# 💡 How HealthHive Works

HealthHive follows an end-to-end safety intelligence workflow:

```text
Worker Reports Hazard / Incident
              ↓
Multilingual / Voice Reporting
              ↓
Speech-to-Text
              ↓
FastAPI Backend
              ↓
AI / NLP Engine
              ↓
SIF Detection + Safety Pattern Analysis
              ↓
IOGP Life-Saving Rule Mapping
              ↓
Confidence Evaluation
              ↓
      ┌───────────────┐
      │               │
High Confidence   Low Confidence
      │               │
      │          HSE Human Review
      │               │
      └───────┬───────┘
              ↓
       Risk Prioritization
              ↓
       PostgreSQL Database
              ↓
       HSE Manager Dashboard
              ↓
      Corrective Action
              ↓
     Closure Verification
              ↓
        Risk Resolved
```

---

# ⭐ Core Features

## 1. 🤖 AI/NLP Safety Analysis

The AI/NLP engine analyzes the text of each safety report and extracts meaningful safety information.

It identifies:

* Hazard descriptions
* Unsafe acts
* Unsafe conditions
* Near-miss situations
* Activities involved
* Potential precursor types
* Barrier/control failures
* Risk indicators

The unstructured report is converted into structured information that can be analyzed and displayed on the HSE dashboard.

---

## 2. 🚨 SIF-Potential Detection

One of the core functions of HealthHive is determining whether a report has **potential for Serious Injury or Fatality (SIF)**.

Each report is evaluated against a defined SIF assessment rubric.

A report is considered potentially SIF-relevant when it indicates a **high-energy source or exposure combined with a critical control that is absent, bypassed, or failed**.


---

## 3. 🏷️ IOGP Life-Saving Rule Mapping

HealthHive maps identified safety situations to relevant **IOGP Life-Saving Rules**.

The same classification process can identify **one or more applicable rules**, allowing multi-label tagging when a single report involves multiple safety risks.

This helps HSE teams understand **which critical safety controls are involved** rather than simply assigning a generic risk level.

---

## 4. 📊 Risk Classification & Prioritization

After analysis, reports are classified according to their risk.

### Risk Levels

| Level         | Meaning                                                       |
| ------------- | ------------------------------------------------------------- |
| 🔴 **High**   | Critical situation requiring immediate attention              |
| 🟡 **Medium** | Significant risk requiring corrective action                  |
| 🟢 **Low**    | Lower-risk observation requiring monitoring or routine action |

The prioritization system helps HSE teams focus their time and resources on the most important safety situations.

---

## 5. 🎯 Recurring Precursor Pattern Detection

HealthHive does more than analyze reports individually.

Structured information extracted from reports—such as **site, activity, precursor type, and barrier/control failure**—can be aggregated to identify recurring patterns.

The dashboard can surface patterns based on:

* Frequency
* Density
* Trends
* Location/site
* Activity
* Precursor type
* Safety rule
* Barrier failure

This allows HSE teams to identify **where fatal potential is repeatedly concentrated** and target preventive interventions accordingly.

---

## 6. 🌐 Multilingual Reporting

Workers can submit safety observations in multiple languages.

HealthHive supports:

* Multilingual text reporting
* Voice-based reporting
* Speech-to-text processing
* Language-aware analysis

This reduces language barriers and makes safety reporting more accessible to workers across different regions.

---

## 7. 🎤 Voice-Based Reporting

Workers can report hazards using their voice instead of typing a detailed report.

### Workflow

```text
Worker speaks
     ↓
Speech-to-Text
     ↓
Text Normalization
     ↓
AI/NLP Analysis
     ↓
SIF & Risk Detection
```

This is particularly useful in industrial environments where workers may need to report an observation quickly.

---

## 8. 👨‍💼 Human-in-the-Loop Review

HealthHive does not blindly trust every AI prediction.

Every AI classification includes a **confidence score**.

When the confidence is below the configured threshold, the report is sent to an **HSE reviewer**.

```text
              AI Analysis
                   ↓
          Confidence Check
                   ↓
        ┌──────────┴──────────┐
        ↓                     ↓
 High Confidence         Low Confidence
        ↓                     ↓
 Automatic Flow          HSE Review
        │                     │
        └──────────┬──────────┘
                   ↓
           Final Classification
```

This reduces the risk of uncertain or potentially incorrect classifications being silently accepted.

A conservative threshold can also ensure that uncertain cases are reviewed rather than automatically dismissed.

---

# 🧠 AI / NLP Engine

The AI/NLP engine is the core intelligence layer of HealthHive.

### Main responsibilities

```text
Safety Report
     ↓
Text Processing
     ↓
Information Extraction
     ↓
SIF Potential Classification
     ↓
Precursor Identification
     ↓
IOGP Rule Mapping
     ↓
Risk Classification
     ↓
Confidence Score
```

The engine uses **LLM/NLP and prompt-based classification** to understand the meaning and context of safety observations.

### Example

**Input:**

> Worker entered a restricted area while equipment was operating without the required isolation.

**Possible AI Output:**

```text
SIF Potential: YES

Risk Level: HIGH

Precursor:
Exposure to high-energy moving equipment

IOGP Rule:
Relevant Life-Saving Rule
```

The result is then sent through the confidence and prioritization workflow.

---

# 🏗️ System Architecture

HealthHive follows a modular architecture consisting of the **worker interface, reporting layer, backend, AI/NLP engine, human review layer, risk prioritizer, database, dashboard, and corrective-action workflow**.

```text
┌──────────────────────────────┐
│         WORKER / USER        │
│                              │
│  Report Hazard / Incident    │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│    MULTILINGUAL REPORTING    │
│                              │
│   Text / Voice / Language    │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│        SPEECH-TO-TEXT        │
│      Voice Reports Only      │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       FASTAPI BACKEND        │
│                              │
│ • Validation                │
│ • Processing                │
│ • REST APIs                 │
└──────────────┬───────────────┘
               ↓
┌────────────────────────────────────┐
│            AI / NLP ENGINE         │
│                                    │
│ • SIF Detection                    │
│ • Precursor Identification         │
│ • IOGP Rule Mapping                │
│ • Risk Classification              │
│ • Confidence Scoring              │
└──────────────────┬─────────────────┘
                   ↓
          ┌────────┴────────┐
          │                 │
          ↓                 ↓
   HIGH CONFIDENCE     LOW CONFIDENCE
          │                 │
          │          ┌──────▼───────┐
          │          │ HSE REVIEW   │
          │          │    QUEUE     │
          │          └──────┬───────┘
          │                 │
          └────────┬────────┘
                   ↓
┌──────────────────────────────┐
│      RISK PRIORITIZER        │
│                              │
│    HIGH / MEDIUM / LOW       │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       POSTGRESQL DB          │
│                              │
│ • Reports                   │
│ • AI Analysis               │
│ • Reviews                   │
│ • Risk Data                 │
│ • Corrective Actions        │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│      HSE MANAGER DASHBOARD   │
│                              │
│ • Risk Overview             │
│ • SIF Precursors            │
│ • Safety Patterns           │
│ • Risk Hotspots             │
│ • Trends & Analytics        │
│ • Review Queue              │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│     CORRECTIVE ACTION        │
│          ASSIGNED            │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│   ACTION COMPLETED +         │
│   CLOSURE VERIFIED           │
└──────────────┬───────────────┘
               ↓
        ┌───────────────┐
        │    CLOSED     │
        │ RISK RESOLVED │
        └───────────────┘
```

---

# 🔄 End-to-End Safety Workflow

### 1. Report

A worker submits an unsafe-act, unsafe-condition, near-miss, or hazard observation.

### 2. Convert

If the report is provided through voice, Speech-to-Text converts it into text.

### 3. Process

The FastAPI backend validates and processes the report.

### 4. Analyze

The AI/NLP engine analyzes the report for SIF potential, precursor patterns, safety rules, and risk.

### 5. Evaluate Confidence

The system checks how confident the AI is in its classification.

### 6. Human Review

Low-confidence cases are sent to HSE professionals.

### 7. Prioritize

The final result is categorized as High, Medium, or Low risk.

### 8. Store

The report and analysis are stored in PostgreSQL.

### 9. Visualize

HSE managers view risks, patterns, hotspots, and trends through the dashboard.

### 10. Act

Corrective actions are assigned to responsible personnel.

### 11. Verify

The HSE team verifies that the corrective action has actually addressed the risk.

### 12. Close

The report is marked as closed once the risk is resolved.

---

# 📈 HSE Manager Dashboard

The dashboard is designed around **risk-focused decision-making** rather than simply displaying a list of reports.

### Key Dashboard Components

**Risk Overview**

* High / Medium / Low risk distribution
* Priority incidents
* Current risk status

**SIF Precursors**

* SIF-potential reports
* Precursor categories
* High-risk observations

**Safety Patterns**

* Recurring precursor types
* Repeated control failures
* Activity-based patterns

**Risk Hotspots**

* Sites or areas with concentrated risk
* Activities with repeated high-risk observations

**Trends & Analytics**

* Risk trends over time
* Frequency of precursors
* Changes in safety patterns

**Human Review Queue**

* Low-confidence AI classifications
* Pending HSE decisions
* Review status

**Corrective Actions**

* Pending actions
* Actions in progress
* Completed actions
* Closure verification

---

# 🛠️ Corrective-Action Management

HealthHive connects **risk identification directly to preventive action**.

```text
Risk Identified
      ↓
Corrective Action Recommended
      ↓
Action Assigned
      ↓
Action In Progress
      ↓
Action Completed
      ↓
HSE Verification
      ↓
Closure Approved
      ↓
Risk Resolved
```

This prevents safety reports from simply being recorded and forgotten.

---

# 📋 Requirement → Solution Mapping

| Requirement                       | How HealthHive Addresses It                                                              |
| --------------------------------- | ---------------------------------------------------------------------------------------- |
| **SIF vs Non-SIF Classification** | AI evaluates reports against a SIF rubric and provides a classification with confidence. |
| **IOGP Life-Saving Rule Tagging** | Reports are mapped to one or more relevant IOGP Life-Saving Rules.                       |
| **Recurring Precursor Patterns**  | Structured report data is aggregated and surfaced through dashboard trends and hotspots. |
| **Large Report Volume**           | AI performs automated first-level analysis and prioritization.                           |
| **Uncertain AI Results**          | Low-confidence cases are routed to HSE experts.                                          |
| **Language Barriers**             | Multilingual and voice-based reporting enables easier worker participation.              |
| **Corrective Actions**            | Actions are assigned, tracked, completed, and verified.                                  |

The first three requirements are central to the system design: SIF classification, IOGP rule tagging, and dashboard-based precursor pattern detection.

---

# 🛠️ Technology Stack

| Category           | Technologies                          | Purpose                                                   |
| ------------------ | ------------------------------------- | --------------------------------------------------------- |
| **Frontend**       | React.js, HTML5, CSS3, JavaScript     | Interactive reporting interface and HSE dashboards        |
| **Backend**        | Python, FastAPI                       | REST APIs, validation, processing and business logic      |
| **AI/NLP**         | Codex 5.6 Terra                       | SIF detection, precursor identification and risk analysis |
| **Speech**         |Codex 5.6 Terra                        | Voice report transcription                                |
| **Database**       | PostgreSQL / Supabase                 | Reports, users, analysis, reviews and corrective actions  |
| **Communication**  | REST API, JSON                        | Frontend-backend communication                            |
| **Authentication** | API-Based Authentication              | Secure platform access                                    |
| **Deployment**     | Vercel, Supabase                      | Cloud deployment                                          |
| **Development**    | Git, GitHub, VS Code, Codex           | Development and version control                           |


# ⚙️ Feasibility

### Technical Feasibility

HealthHive uses established technologies such as React, FastAPI, PostgreSQL, Speech-to-Text, and existing AI/NLP capabilities, making the solution practical to develop and deploy.

### Operational Feasibility

The worker interface is designed to make reporting quick and simple, particularly in demanding industrial environments.

### Economic Viability

Automation can reduce the effort required for manual report analysis and help organizations focus resources on the most critical risks.

---

# 📈 Scalability

The modular architecture allows HealthHive to expand across:

* Multiple industrial sites
* Departments
* Languages
* Larger report volumes
* Additional HSE workflows

The AI/NLP, dashboard, database, and corrective-action components can also be enhanced independently as the platform grows.

---

# 🌟 Impact & Benefits

* ⚡ Faster safety reporting
* 🚨 Earlier identification of high-risk situations
* 🎯 Better SIF precursor detection
* 🏷️ Standardized safety-rule mapping
* 📊 Data-driven HSE decision-making
* 👨‍💼 Reduced manual analysis
* 🌐 Improved multilingual accessibility
* 🔍 Identification of recurring safety patterns
* 🛠️ Better corrective-action tracking
* ✅ Verified risk closure
* 🛡️ More proactive workplace safety

---

# 🚀 Future Scope

HealthHive can be extended with:

* Advanced ML-based risk prediction
* Additional Indian and regional languages
* Improved speech recognition
* IoT and workplace sensor integration
* Computer-vision-based hazard detection
* Predictive safety analytics
* Advanced risk heatmaps
* Integration with existing enterprise HSSE systems
* Continuous model improvement using reviewed reports

