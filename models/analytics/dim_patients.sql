{{ config(materialized='view') }}

SELECT DISTINCT
    patient_id,
    gender,
    age,
    insurance_type
FROM {{ source('raw', 'raw_admissions') }}

