import pandas as pd
from google.cloud import bigquery
import os

# --- CONFIGURATION ---
PROJECT_ID = "effidic-stage-2026"
DATASET_ID = "raw_energy"
TABLE_ID = "conso_quotidienne"
CSV_PATH = "../data/conso_elec.csv"

def load_data_to_bigquery():
    print(f"🚀 Démarrage de l'ingestion de {CSV_PATH} vers BigQuery...")

    # 1. Lire le CSV avec Pandas
    try:
        # low_memory=False évite les warnings sur les types mixtes
        df = pd.read_csv(CSV_PATH, sep=';', low_memory=False)
        print(f"✅ Fichier lu avec succès : {len(df)} lignes trouvées.")
    except Exception as e:
        print(f"❌ Erreur de lecture CSV : {e}")
        return

    # 2. Nettoyage ROBUSTE des colonnes
    # BigQuery n'accepte que des lettres, chiffres et underscores. Pas de parenthèses !
    df.columns = (df.columns
                  .str.replace(' ', '_')
                  .str.replace('é', 'e')
                  .str.replace('è', 'e')
                  .str.replace("'", "")
                  .str.replace("(", "")   # <--- NOUVEAU : Supprime (
                  .str.replace(")", "")   # <--- NOUVEAU : Supprime )
                  .str.replace(".", "")   # <--- NOUVEAU : Supprime les points
                  .str.replace("-", "_")  # <--- NOUVEAU : Remplace tirets par underscores
                  .str.lower())
    
    print("✅ Colonnes nettoyées (parenthèses supprimées).")

    # 3. Connexion à BigQuery
    try:
        client = bigquery.Client(project=PROJECT_ID)
        table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

        # Configuration du job
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE",
            autodetect=True,
        )

        # 4. Envoi des données
        print("⏳ Envoi vers BigQuery en cours (cela peut prendre 1 à 2 minutes)...")
        job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
        job.result()  # Attend la fin du job
        
        print(f"🎉 Succès ! Les données sont chargées dans {table_ref}")
        
        # Vérification
        table = client.get_table(table_ref)
        print(f"📊 La table contient maintenant {table.num_rows} lignes.")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'upload BigQuery : {e}")

if __name__ == "__main__":
    load_data_to_bigquery()