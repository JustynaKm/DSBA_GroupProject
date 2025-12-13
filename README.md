# DSBA_GroupProject
Data Science and Business Analytics Module - Group Assignment
This project demonstrates the design and implementation of an analytics-ready data model for CRM (Salesforce) opportunity data and other relevant CSV files using Snowflake.

The goal is to integrate and unify all data files into one data platform  and transform this raw, operational CRM data into  actionable, predictive, and decision-ready insights that are visualized in Powerbi dashboard

Instead of relying on static pipeline reporting or subjective deal stages, this project answers:

- Which opportunities are truly healthy?
- Which deals should sales leaders prioritize?
- Which behavioral and qualification signals predict success early?
- How much revenue is realistically expected, not just forecasted?

⚠️ **Important:**  
All data used in this project is **synthetic**, designed to realistically simulate enterprise CRM complexity while remaining fully compliant and non-sensitive.

---

## 🧩 Business Problem

CRM data is typically stored in multiple operational tables that are:
- Highly duplicated
- Poorly structured for analytics
- Difficult to query consistently

Business users need reliable answers to questions such as:
- Which account groupings generate the highest value?
- How long do opportunities remain in each sales stage?
- What actions or next steps correlate with successful deal closures?

This project addresses these challenges by applying data warehousing best practices.

---

## 🏗️ Architecture Overview

The solution follows a layered architecture:

### 1️⃣ RAW Layer
- Mirrors source CRM data with no transformations
- Preserves data lineage and traceability
- Ingested automatically via ETLeap

Tables include:
- `OPEN_OPPORTUNITIES_RAW`
- `CLOSED_OPPORTUNITIES_RAW`
- `ACCOUNT_GROUPING_RAW` -> via Etleap Plugin connecting Snowflake to CRM Salesforce
- `NEXT_STEPS_HISTORY_OPEN_RAW`
- `NEXT_STEPS_HISTORY_CLOSED_RAW`

---

### 2️⃣ MODEL Layer
- Analytics-optimized schema
- Deduplication and surrogate keys
- Clear separation of facts and dimensions

Core objects:
- **DIM_ACCOUNT_GROUPING**
- **FACT_OPPORTUNITIES**
- **FACT_NEXT_STEPS**

---

## 🗂️ Data Modeling Approach

### Dimensional Modeling
- Account Groupings modeled as a dimension
- Opportunities and historical next steps modeled as facts
- Natural keys retained for traceability
- Surrogate keys used for joins and performance

### Key Design Decisions
- Separate RAW and MODEL layers
- Views used in MODEL layer for automatic refresh
- Two fact tables to preserve different granularities:
  - Opportunity-level facts
  - Event-level historical facts

---

## 🔄 Data Refresh Strategy

- Source data refreshed hourly via ETLeap
- MODEL layer implemented using views
- Ensures near real-time analytics without reprocessing overhead

---

## 📊 Analytics Readiness and Power BI

The Reporting Tools:

→ Python & Snowpark  
→ Snowflake (RAW → CURATED schemas)  
→ Feature Engineering (SQL + Python)  
→ Machine Learning (XGBoost)  
→ Predictions written back to Snowflake  
→ Power BI dashboards (live connection)

Snowflake acts as the **central data platform**, powering analytics, ML, and visualization from a single source of truth.


The MODEL layer supports:
- KPI calculation
- Time-in-stage analysis
- Opportunity funnel analysis
- Account-level performance reporting

The model is fully compatible with BI tools such as Power BI.

**Feature Engineering (Core Intelligence)**

Rather than using raw CRM fields, we engineered **behavioral, quality, and benchmark-driven signals**.

----selected KPIs---

**Early Stage Health (Benchmark-Based)**
- Evaluates only **open opportunities**
- Benchmarks stage performance (stages 0–3) against **historical closed-won deals**
- Benchmarks are computed by **account grouping**
- Purpose: detect deals that appear fine but are already lagging behind winners

**Next Steps Hygiene**
Derived from next-step history across all stages:
- Number of updates
- Average days between updates
- Text similarity between consecutive updates

This captures **deal momentum and execution quality**, identifying stalled, copy-paste, or actively progressed deals.

**Need AI (Discovery Quality)**
An AI-driven score evaluates whether customer needs are:
- Clearly articulated
- Business-problem oriented
- More than product mentions

This replaces naive “field filled” logic with **semantic quality assessment**.

**Champion & Role Fit AI**
Analyzes whether opportunity contacts align with:
- Economic buyers
- True champions (LOB owners, senior decision makers)

Outputs role-fit and champion-fit signals that convert titles into **decision authority indicators**.

**MEDDPICC Qualification Score**
Quantifies how well opportunities are qualified across MEDDPICC dimensions, producing a single numeric score instead of binary flags.

**Competitive Strength**
Measures historical success against competitors by account grouping to capture competitive context.

---

**Machine Learning Model**
**Objective**
Predict **win probability** for open opportunities.

**Model Choice**
- **XGBoost Classifier**
- Selected for:
  - Strong performance on tabular business data
  - Ability to model non-linear interactions
  - Robust handling of mixed numeric and categorical features

**Training Strategy**
- Training data: closed opportunities only
- Target variable: won vs lost
- Train/test split: 80/20
- Class imbalance handled using `scale_pos_weight`

**Model Performance**
- ROC-AUC ≈ **0.80–0.82**

ROC-AUC measures **ranking quality**, not raw accuracy.  
This is the correct metric for prioritization and forecasting use cases.

**Model Output**
Predicted win probabilities for open opportunities are written back to Snowflake and bucketed into:
- High
- Medium
- Low

---

**Power BI Dashboard**

Power BI connects directly to Snowflake curated views.

**Key Insights Shown**
- Pipeline waterfall (raw vs probability-weighted revenue)
- Distribution of win probabilities
- Early stage health vs historical benchmarks
- Next steps hygiene (execution quality)
- Top open opportunities with all AI signals combined

Each visual answers **one specific business question** and supports faster, evidence-based decision making.

---
**Live Platform Demonstration**

Because Snowflake is the central platform:
- SQL updates propagate instantly to Power BI
- No file movement or manual refresh pipelines
- Demonstrates real-time analytics and decision support
---

## 🛠️ Technologies Used

- Snowflake
- ETLeap
- SQL
- Dimensional Modeling
- Mermaid ER Diagrams
- Python
- Power BI
- Microsoft Office (CSV Files)
- Built-in Snowflake functions including Snowpark and LLM

---

## 👤 Authors: Justyna Kmiecik and Emna Makni

This project was developed as part of an academic analytics assignment to demonstrate real-world data engineering and modeling practices.
