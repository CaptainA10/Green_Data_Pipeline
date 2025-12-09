# Intégration Apache Airflow - Green Energy Pipeline

Ce dossier contient la configuration complète pour orchestrer le pipeline de données Green Energy avec Apache Airflow, sécurisé par une clé de service GCP.

## 📂 Structure des Fichiers

```
airflow/
├── dags/
│   └── green_energy_dag.py       # Le DAG principal (Ingest -> Prep -> Load -> dbt)
├── scripts/
│   ├── fetch_weather.py          # Récupération API Open-Meteo (JSON brut)
│   ├── process_weather.py        # Nettoyage et conversion CSV
│   └── load_weather_to_bq.py     # Chargement BigQuery
├── keys/
│   └── service-account.json      # VOTRE CLÉ GCP (à ajouter, ignorée par git)
├── docker-compose.yaml           # Orchestration (Webserver, Scheduler, Postgres)
├── Dockerfile                    # Image personnalisée (Airflow + dbt + GCP libs)
├── profiles.yml                  # Configuration dbt pour Airflow
├── requirements.txt              # Dépendances Python
└── README.md                     # Ce fichier
```

## 🔑 Configuration de la Clé GCP

**CRITIQUE :** Vous devez placer votre fichier de clé JSON dans le dossier `keys/`.

1.  Créez le dossier s'il n'existe pas :
    ```bash
    mkdir -p airflow/keys
    ```
2.  Copiez votre clé JSON à l'intérieur et renommez-la **exactement** en `service-account.json`.
    - Chemin final : `airflow/keys/service-account.json`
3.  **Sécurité** : Ce fichier est automatiquement ignoré par `.gitignore` (si configuré à la racine) pour ne pas être commité. Vérifiez votre `.gitignore` racine :
    ```text
    airflow/keys/
    *.json
    ```

## 🚀 Lancement du Pipeline

1.  **Construction de l'image** :
    ```bash
    cd airflow
    docker-compose build
    ```

2.  **Initialisation** (Premier lancement uniquement) :
    ```bash
    docker-compose up airflow-init
    ```

3.  **Démarrage** :
    ```bash
    docker-compose up -d
    ```

4.  **Accès UI** : [http://localhost:8080](http://localhost:8080) (Logins: `admin` / `admin`).

## 🧪 Test du Pipeline

1.  Activez le DAG `green_energy_pipeline` dans l'interface.
2.  Déclenchez-le manuellement (Bouton "Trigger DAG").
3.  Vérifiez les logs :
    - **Ingest** : Doit sauvegarder `raw_weather.json`.
    - **Prepare** : Doit créer `weather_data.csv`.
    - **Load** : Doit charger dans `effidic-stage-2026.raw_energy.daily_weather`.
    - **dbt** : Doit exécuter `dbt run` et `dbt test` avec succès.

## 🛠 Détails Techniques

- **Source** : Open-Meteo API (Données météo Paris, historiques et journalières).
- **BigQuery** : Table `raw_energy.daily_weather` (Mode `WRITE_TRUNCATE` pour la démo, n'écrase pas vos autres tables).
- **dbt** : Utilise le profil `green_energy` défini dans `airflow/profiles.yml`, pointant vers le dataset `green_energy_dbt` (ou celui configuré).
