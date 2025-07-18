{{ config(materialized='view') }}


SELECT
    A.patient_id,
    A.admission_id,
    A.bed_id,
    A.department,
    A.admission_type,
    A.primary_diagnosis,
    A.admit_time,
    D.discharge_time,
    D.discharge_status,
    D.length_of_stay,
    D.discharge_destination
FROM {{ source('raw', 'raw_admissions') }} A
LEFT JOIN {{ source('raw', 'raw_discharges') }} D
    ON A.patient_id = D.patient_id AND A.admission_id = D.admission_id
