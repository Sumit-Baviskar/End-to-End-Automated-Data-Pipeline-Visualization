{{ config(materialized='view') }}

SELECT DISTINCT
    bed_id,
    bed_type,
    room_number,
    is_critical_care,
    department
FROM {{ source('raw', 'raw_bed_inventory') }}

