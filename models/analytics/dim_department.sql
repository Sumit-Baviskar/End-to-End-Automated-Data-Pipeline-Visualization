{{ config(materialized='view') }}

SELECT DISTINCT
    DEPARTMENT
FROM {{ source('raw', 'raw_admissions') }}

UNION

SELECT DISTINCT
    FROM_DEPARTMENT
FROM {{ source('raw', 'raw_transfers') }}

UNION

SELECT DISTINCT
    DEPARTMENT
FROM {{ source('raw', 'raw_bed_inventory') }}
