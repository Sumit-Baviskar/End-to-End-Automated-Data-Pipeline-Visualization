{{ config(materialized='view') }}


SELECT
    patient_id,
    admission_id,
    transfer_time,
    from_department,
    to_department,
    reason
FROM {{ source('raw', 'raw_transfers') }}
