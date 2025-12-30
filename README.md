# Green Energy Data Engineering Project

End-to-end Modern Data Stack project delivering reliable, analytics-ready KPIs for renewable energy monitoring and decision support.

[![Live Dashboard](https://img.shields.io/badge/Live_Dashboard-Looker_Studio-brightgreen?style=for-the-badge)](https://lookerstudio.google.com/s/u-64-Hc96RQ)
[![Live Demo](https://img.shields.io/badge/Live_Demo-Application-brightgreen?style=for-the-badge)](https://your-demo-link.com)

---

## Project Overview

This project implements a production-oriented ELT data pipeline that transforms raw renewable energy datasets into trusted analytical models.  
It follows modern data engineering best practices, including cloud-native data warehousing, transformation-as-code, automated data quality checks, and BI-ready data modeling.

The resulting data supports regional and temporal analysis to help stakeholders monitor renewable energy adoption and consumption trends in the context of energy transition.

---

## Architecture

```mermaid
flowchart LR
    A[Raw Energy Data<br/>CSV Files]
    B[Python Ingestion Layer]
    C[BigQuery<br/>Raw Dataset]
    D[dbt Core<br/>Transformations & Tests]
    E[BigQuery<br/>Analytics Dataset]
    F[Looker Studio<br/>Dashboard]
    G[Live Demo<br/>Application]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    E --> G
Architecture Components
Layer	Technology	Responsibility
Ingestion	Python	Load raw data into BigQuery
Storage	BigQuery	Serverless cloud data warehouse
Transformation	dbt Core	Modeling, cleaning, KPI creation
Data Quality	dbt Tests	Automated validation and integrity checks
Analytics	Looker Studio	BI dashboards and reporting
Consumption	Live Demo	External data consumption

Key Features
End-to-end Modern Data Stack implementation

Automated ELT pipeline

Cloud-native data warehouse (BigQuery)

Modular and versioned dbt data models

Automated data quality testing (DataOps approach)

Analytics-ready KPI tables

Time-series and year-over-year analysis

Interactive dashboards for decision support

Reproducible and version-controlled environment

Data Model and KPIs
Final Analytics Table
dbt_production.kpi_region_mensuel

Core Metrics
Renewable energy share (%)

Total energy consumption (GWh)

Analytical Dimensions
Region

Year

Month

This table is optimized for Business Intelligence tools and downstream analytics use cases.

Data Quality and Testing
Data reliability is enforced through automated dbt tests, including:

not_null constraints on critical dimensions

KPI consistency and validity checks

All critical tests pass successfully, ensuring trusted analytical outputs.

Dashboard
The Looker Studio dashboard provides:

Regional comparison of renewable energy adoption

Monthly and yearly trend analysis

Monitoring of key energy performance indicators

Live dashboard:
https://lookerstudio.google.com/s/u-64-Hc96RQ

Tech Stack
Languages
Python 3.10+

SQL (BigQuery Standard SQL)

Data and Analytics
Google BigQuery

dbt Core

Looker Studio

Engineering and Tooling
Git / GitHub

Bash

Python virtual environments

Installation and Setup
bash
Copier le code
# Clone the repository
git clone https://github.com/CaptainA10/Green_Data_Pipeline.git
cd Green_Data_Pipeline/green_energy

# Install dependencies
pip install -r requirements.txt
dbt deps

# Run transformations and tests
dbt run
dbt test
BigQuery Configuration
Create or update ~/.dbt/profiles.yml:

yaml
Copier le code
green_energy:
  target: dev
  outputs:
    dev:
      type: bigquery
      method: service-account
      keyfile: path/to/service-account.json
      project: your-project-id
      dataset: dbt_production
      threads: 4
Deployment
Create the dbt_production dataset in BigQuery

Ingest raw datasets using Python ingestion scripts

Execute dbt transformations locally or via CI/CD pipelines

Publish Looker Studio dashboards

Deploy and expose the live demo application

Author
NGUETTE FANE Gad
Data Engineering Student – Cloud and Analytics

Email: nguettefanegad@gmail.com
