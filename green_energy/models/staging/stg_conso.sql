with source as (
    select * from {{ source('raw_energy', 'daily_weather') }}
),

renamed as (
    select
        -- Mapping de la date
        date as date_reference,
        
        -- Simulation de la région (Données Paris -> Île-de-France)
        '11' as code_insee_region,
        'Île-de-France' as region,
        
        -- Simulation de la Consommation basée sur la température (Modèle simple : + froid = + chauffage)
        -- Hypothèse : Base 2000 MW + 1000 MW par degré sous 20°C
        GREATEST(2000, (20 - SAFE_CAST(min_temp_c AS FLOAT64)) * 1000 + 2000) as consommation_mw,
        
        -- Simulation du Nucléaire (Base stable)
        5000 as production_nucleaire_mw,
        
        -- Simulation de l'Eolien (Basé sur le vent)
        -- Hypothèse : 50 MW par km/h de vent
        coalesce(SAFE_CAST(max_wind_speed_kmh AS FLOAT64) * 50, 0) as production_eolienne_mw,
        
        -- Simulation du Solaire (Basé sur la radiation)
        -- Hypothèse : 100 MW par MJ/m²
        coalesce(SAFE_CAST(solar_radiation_mj_m2 AS FLOAT64) * 100, 0) as production_solaire_mw,
        
        -- Autres sources à 0 pour ce MVP
        0 as production_thermique_mw,
        0 as production_hydraulique_mw,
        0 as production_bioenergies_mw

    from source
)

select * from renamed