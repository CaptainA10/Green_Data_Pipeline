\# 🌿 Projet Data Engineer - Analyse Énergétique Verte (EFFIDIC)



Bienvenue sur le dépôt du pipeline de données "Green Energy". Ce projet implémente une \*\*Modern Data Stack (MDS)\*\* complète et industrialisée, suivant le modèle \*\*ELT (Extract, Load, Transform)\*\* pour ingérer, transformer et visualiser les données de production et consommation d'énergie renouvelable.



---

\## 1. Objectifs et Architecture



\### 🎯 Objectif

Le but est de traiter des données brutes de consommation énergétique pour calculer des \*\*KPIs décisionnels granulaires\*\* (agrégation par Région et par Mois). L'objectif est de fournir une base analytique permettant de \*\*piloter la transition énergétique\*\* et d'effectuer des comparaisons \*\*Année-sur-Année (YoY)\*\*.



\### 🏗️ Architecture Technique (Modern Data Stack)

L'architecture utilise des outils "best-of-breed" pour garantir scalabilité, performance et maintenance :

\* \*\*Ingestion (E \& L) :\*\* Script \*\*Python\*\* pour la migration des fichiers locaux (CSV) vers le Cloud.

\* \*\*Data Warehouse :\*\* \*\*Google BigQuery\*\* (serverless) pour le stockage scalable et l'exécution des requêtes SQL de transformation.

\* \*\*Transformation (T) :\*\* \*\*dbt (data build tool)\*\* pour la modélisation des données, le nettoyage, et la création de dimensions analytiques (`annee`, `mois\_chiffre`).

\* \*\*Visualisation :\*\* \*\*Looker Studio\*\* pour le reporting final.

\* \*\*Infrastructure/Mise en Production :\*\* Git, Bash, et un environnement virtuel Python.



!\[Architecture du Pipeline](docs/1\_schema\_architecture.png)



---

\## 2. Résultats \& KPIs



La transformation dbt génère une table finale optimisée pour l'analyse, la table \*\*`dbt\_production.kpi\_region\_mensuel`\*\*.



\### 📊 Modélisation Analytique

La modélisation sépare les dimensions temporelles (`annee`, `mois\_chiffre`) pour faciliter les analyses de séries temporelles :

1\.  \*\*Part Renouvelable (%) :\*\* `part\_renouvelable\_pourcentage` (Moyenne pondérée par région).

2\.  \*\*Consommation Totale :\*\* Volume global agrégé en GWh.



\### 📈 Visualisation (Dashboard)

Le tableau de bord ci-dessous illustre non seulement la disparité de la production verte entre les régions (classement), mais aussi la \*\*tendance annuelle (YoY)\*\* grâce à la modélisation dimensionnelle.



!\[Dashboard Looker Studio](docs/3\_dashboard\_looker.png)



---

\## 3. Qualité des Données (DataOps)



La fiabilité de la table `dbt\_production.kpi\_region\_mensuel` est garantie par une suite de tests automatisés (DataOps) exécutée par dbt.



\* \*\*Tests exécutés :\*\* `not\_null` (sur toutes les clés primaires et dimensions critiques : `region`, `mois\_cle`, `annee`), et tests sur les indicateurs.

\* \*\*Statut actuel :\*\* ✅ \*\*PASS\*\* (\*\*5 tests critiques validés\*\*).



!\[Preuve d'exécution dbt](docs/2\_proof\_dbt\_run\_test.png)



---

\## 🚀 Comment exécuter ce projet



Ces commandes doivent être exécutées depuis le répertoire `green\_energy/`.



```bash

\# 1. Cloner le repo

git clone \[url-du-repo]

cd \[nom-du-repo]/green\_energy



\# 2. Installer les dépendances (Python et dbt packages)

pip install -r requirements.txt

dbt deps



\# 3. Lancer la transformation et les tests

\# Ceci crée/met à jour les vues dans BigQuery et exécute les tests de qualité.

dbt run

dbt test

