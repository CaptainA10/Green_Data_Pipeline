with source as (
    select * from {{ source('raw_energy', 'conso_quotidienne') }}
),

renamed as (
    select
        -- Date corrigée précédemment
        date___heure as date_reference, 
        code_insee_region,
        region,
        
        -- Noms réels de BigQuery (à gauche) aliasés vers des noms explicites (à droite)
        coalesce(consommation_mw, 0) as consommation_mw,
        
        -- Corrections (On utilise le nom réel de BigQuery)
        coalesce(nucleaire_mw, 0) as production_nucleaire_mw,
        
        -- CORRECTION CRUCIALE : SAFE_CAST pour convertir le STRING en FLOAT
        coalesce(SAFE_CAST(eolien_mw AS BIGNUMERIC), 0) as production_eolienne_mw,
        
        coalesce(solaire_mw, 0) as production_solaire_mw,
        
        -- On conserve les autres colonnes utiles pour info
        coalesce(thermique_mw, 0) as production_thermique_mw,
        coalesce(hydraulique_mw, 0) as production_hydraulique_mw,
        coalesce(bioenergies_mw, 0) as production_bioenergies_mw
    from source
)

select * from renamed