with daily_data as (
    select
        date_reference,
        code_insee_region,
        region,
        
        -- Extraction du format AAAA-MM (utilisé pour le tri)
        SUBSTR(date_reference, 1, 7) as mois_annee_texte, 
        
        -- Extraction de l'Année (AAAA) comme Entier
        CAST(SUBSTR(date_reference, 1, 4) AS INT64) as annee, 
        
        -- Extraction du Mois (MM) comme Entier
        CAST(SUBSTR(date_reference, 6, 2) AS INT64) as mois_chiffre, 
        
        -- Conversion sécurisée en FLOAT pour garantir les calculs
        CAST(consommation_mw AS FLOAT64) as consommation_mw,
        CAST(production_nucleaire_mw AS FLOAT64) as production_nucleaire_mw,
        CAST(production_eolienne_mw AS FLOAT64) as production_eolienne_mw,
        CAST(production_solaire_mw AS FLOAT64) as production_solaire_mw

    from {{ ref('stg_conso') }}
),

monthly_kpi as (
    select
        mois_annee_texte as mois_cle, -- Champ texte complet pour le tri temporel
        annee,                       -- NOUVELLE COLONNE pour la segmentation Looker
        mois_chiffre,                -- NOUVELLE COLONNE pour l'axe X (mois 1 à 12)
        region,
        
        -- Calculs des KPIs
        round(avg(consommation_mw), 2) as conso_moyenne_mw,
        round(sum(consommation_mw) / 1000, 2) as conso_totale_gw,
        
        -- Calcul du mix énergétique (Part du vert)
        round(
            sum(production_eolienne_mw + production_solaire_mw) / nullif(sum(consommation_mw), 0) * 100
        , 2) as part_renouvelable_pourcentage

    from daily_data
    -- Les champs annee et mois_chiffre doivent être inclus ici pour le regroupement
    group by 1, 2, 3, 4 
)

select * from monthly_kpi
order by mois_cle desc, conso_totale_gw desc