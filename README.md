# DSBA_GroupProject
Data Science and Business Analytics Module - Group Assignment
This project demonstrates the design and implementation of an analytics-ready data model for CRM (Salesforce) opportunity data using Snowflake.

The goal is to transform raw, operational CRM data into a clean, structured model suitable for business intelligence and decision-making.

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

## 📊 Analytics Readiness

The MODEL layer supports:
- KPI calculation
- Time-in-stage analysis
- Opportunity funnel analysis
- Account-level performance reporting

The model is fully compatible with BI tools such as Power BI.

---

## 🚀 Future Improvements

- Add a Date Dimension
- Introduce Opportunity Status Dimension
- Implement snapshot fact tables
- Apply predictive analytics for deal success

---

## 🛠️ Technologies Used

- Snowflake
- ETLeap
- SQL
- Dimensional Modeling
- Mermaid ER Diagrams

---

## 👤 Authors: Justyna Kmiecik and Emna Makni

This project was developed as part of an academic analytics assignment to demonstrate real-world data engineering and modeling practices.
