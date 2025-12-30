# Green Energy Data Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![BigQuery](https://img.shields.io/badge/BigQuery-Cloud-orange.svg)
![dbt](https://img.shields.io/badge/dbt-Core-red.svg)
![License](https://img.shields.io/badge/License-Academic-green.svg)

## Architecture du Système

### Flux de Données

```
Raw Energy Data (CSV Files) 
    ↓
Python Ingestion Layer
    ↓
BigQuery Raw Dataset
    ↓
dbt Core (Transformations & Tests)
    ↓
BigQuery Analytics Dataset
    ↓
Looker Studio Dashboard / Live Demo Application
```

## Composants de l'Architecture

| Layer | Technology | Responsibility |
|-------|-----------|----------------|
| Ingestion | Python | Load raw data into BigQuery |
| Storage | BigQuery | Serverless cloud data warehouse |
| Transformation | dbt Core | Modeling, cleaning, KPI creation |
| Data Quality | dbt Tests | Automated validation and integrity checks |
| Analytics | Looker Studio | BI dashboards and reporting |
| Consumption | Live Demo | External data consumption |

## Fonctionnalités Principales

- End-to-end Modern Data Stack implementation
- Automated ELT pipeline
- Cloud-native data warehouse (BigQuery)
- Modular and versioned dbt data models
- Automated data quality testing (DataOps approach)
- Analytics-ready KPI tables
- Time-series and year-over-year analysis
- Interactive dashboards for decision support
- Reproducible and version-controlled environment

## Modèle de Données et KPI

### Table Analytique Finale

`dbt_production.kpi_region_mensuel`

### Métriques Principales

- Renewable energy share (%)
- Total energy consumption (GWh)

### Dimensions Analytiques

- Region
- Year
- Month

This table is optimized for Business Intelligence tools and downstream analytics use cases.

## Qualité des Données et Tests

Data reliability is enforced through automated dbt tests, including:

- not_null constraints on critical dimensions
- KPI consistency and validity checks

All critical tests pass successfully, ensuring trusted analytical outputs.

## Dashboard

The Looker Studio dashboard provides:

- Regional comparison of renewable energy adoption
- Monthly and yearly trend analysis
- Monitoring of key energy performance indicators

Live dashboard: [https://lookerstudio.google.com/s/u-64-Hc96RQ](https://lookerstudio.google.com/s/u-64-Hc96RQ)

## Stack Technique

### Langages

- Python 3.10+
- SQL (BigQuery Standard SQL)

### Données et Analytics

- Google BigQuery
- dbt Core
- Looker Studio

### Ingénierie et Outils

- Git / GitHub
- Bash
- Python virtual environments

## Installation et Configuration

```bash
# Clone the repository
git clone https://github.com/CaptainA10/Green_Data_Pipeline.git
cd Green_Data_Pipeline/green_energy

# Install dependencies
pip install -r requirements.txt
dbt deps

# Run transformations and tests
dbt run
dbt test
```

## Configuration BigQuery

Create or update `~/.dbt/profiles.yml`:

```yaml
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
```

## Déploiement

1. Create the `dbt_production` dataset in BigQuery
2. Ingest raw datasets using Python ingestion scripts
3. Execute dbt transformations locally or via CI/CD pipelines
4. Publish Looker Studio dashboards
5. Deploy and expose the live demo application

## Liens

- Repository: [https://github.com/CaptainA10/Green_Data_Pipeline](https://github.com/CaptainA10/Green_Data_Pipeline)
- Live Dashboard: [https://lookerstudio.google.com/s/u-64-Hc96RQ](https://lookerstudio.google.com/s/u-64-Hc96RQ)

## Auteur

**NGUETTE FANE Gad**

Data Engineering Student – Cloud and Analytics

Email: nguettefanegad@gmail.com
