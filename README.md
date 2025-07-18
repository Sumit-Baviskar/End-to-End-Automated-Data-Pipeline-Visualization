# **End to End Automated Data Pipeline Visualization :**

Welcome! This repository showcases a comprehensive, domain-agnostic data engineering and analytics project designed to demonstrate the power of automation, modern data pipelines, and real-time business intelligence.

In this project, I built a fully automated, end-to-end data pipeline that moves data from raw storage (Amazon S3) into a cloud data warehouse (Snowflake), transforms it using dbt (data build tool), and delivers clean, analytics-ready data models for visualization in BI tools such as Power BI or AWS QuickSight.

The project simulates hospital operational data, including admissions, discharges, transfers, and bed inventory. However, the design is fully flexible and can be adapted to any industry, including retail, logistics, finance, or manufacturing.


## 🚀 **Why This Project?**

Organizations often struggle with fragmented data sources, manual reporting processes, and lack of real-time insights. This project addresses these challenges by:

 - Automating data ingestion and transformation workflows
 
 - Reducing manual intervention and errors
 
 - Providing near real-time visibility into key operational metrics
 
 - Enabling data-driven decision-making through interactive dashboards



## **💬 Architecture Layers :**


### 1️⃣ **Data Ingestion Layer** : Central raw data repository before processing.
  
   - Storage: Amazon S3 bucket (e.g., s3://12-7-2025--hospital-data)


### 2️⃣ **Data Warehouse Layer** : Using Snowflake Platform.

   - **Raw schema (HOSPITAL.RAW)**: Stores directly ingested tables from S3

     Example tables:

        - RAW_ADMISSIONS

        - RAW_DISCHARGES

        - RAW_BED_INVENTORY

        - RAW_TRANSFERS

   - Load files using Snowflake's COPY INTO command from S3.

 


 ### 3️⃣ **Transformation Layer :** Using dbt (Data Build Tool) tool.

   - Transform raw tables into clean staging models

       -  Example dbt models

           - stg_admissions.sql

           - stg_discharges.sql

           - stg_bed_inventory.sql

int_patient_journey.sql (integrated table combining admissions and discharges)

  - **Build Gold Layer (Analytics-ready) :**

      - **Dimension tables**

          - dim_patient

          - dim_department

          - dim_bed

      - **Fact tables**

          - fact_admission_events

          - fact_transfer_events

## **Flowchart :**

     Raw Layer (Admissions, Discharges, Transfers)
         │
         ▼
     Transform in Python/DBT → Load to Snowflake
         │
         ├───> Dimension Tables: dim_patient, dim_bed, dim_department
         │
         └───> Fact Tables: fact_admission_events, fact_transfer_events


### 4️⃣ Visualization & Analytics Layer : Using AWS QuickSight or Power BI for Building Dashboard.
   - **Tools: AWS QuickSight or Power BI**
     

## 💡 **What This Project Demonstrates**

✅ Cloud-based data storage and warehouse integration (S3 + Snowflake)  

✅ Modular, automated data transformations using dbt (raw → staging → analytics-ready models)  

✅ Design of fact and dimension tables for robust analytics and reporting  

✅ Creation of operational and strategic KPIs (e.g., bed occupancy rate, readmission rate, patient flow trends)  

✅ Interactive dashboards for business users to analyze and monitor operations in real time  

✅ Scalable and reusable architecture that can be extended to any domain or dataset


## **Architecture Flow (Step-by-Step) :**

### 1️⃣ **S3 → Snowflake (Initial load) :**

   - Data in S3: Raw CSVs (admissions, discharges, transfers, bed inventory).

   - Action: Use Snowflake external stage and COPY INTO to load data into Snowflake raw tables.

###  2️⃣ **Snowflake → DBT :**
    
   - In Snowflake: You have raw tables (staging layer).

   - DBT connects to Snowflake and transforms raw data → creates cleaned, modeled tables (like dimension tables, fact tables).

###  3️⃣ **DBT → Snowflake (Refined layer) :**

   - After DBT runs, modeled (transformed) tables and views are materialized in Snowflake.

   ### ✅  Tables included

   - **Dimension tables**

       - dim_patient

       - dim_department

       - dim_bed

   - **Fact tables**

       - fact_admission_events

       - fact_transfer_events

   - These become your gold layer tables (cleaned and ready for analytics).


### 📁 **FOLDER STRUCTURE (DBT PROJECT) :**

    hospital_data_pipeline/
    │
    ├── dbt_project.yml               # Project config
    ├── packages.yml                  # Optional packages
    ├── README.md                     # Project readme
    │
    ├── models/                       # All DBT models go here
        ├── staging/                  # Stage tables (from raw Snowflake schema)
        │   ├── stg_admissions.sql
        │   ├── stg_beds.sql
        │   └── stg_transfers.sql
        │
        ├── analytics/                    # Final models (fact + dim)
            ├── dim/                  
            │   ├── dim_patients.sql
            │   ├── dim_beds.sql
            │   └── dim_departments.sql
            │
            └── fact/
              ├── fact_admissions.sql
              ├── fact_transfer_events.sql
              └── fact_bed_occupancy.sql
        
 






### 4️⃣ **Snowflake → S3 (Export for sharing) :**

   - Export final fact and dimension tables back to S3 using COPY INTO and external stages.

   - Purpose: Archive, share with data lake users, or downstream tools.


### 5️⃣ **S3 → Glue :**

   - AWS Glue crawlers scan exported CSV files in S3, create Glue catalog tables.

   - These are now structured and queryable in AWS.

### 6️⃣ **Glue → Athena :**

   - Athena queries the data directly from S3 (via Glue catalog).

   - You can run SQL-like queries on fact and dimension tables without moving data.


### 7️⃣ **Athena → QuickSight :**

   - Connect QuickSight to Athena as the data source.

   - Build interactive dashboards on top of the data (example: bed utilization, admissions trends, transfers).


## 🌟 **Key Highlights**

- **Fully Automated Pipeline:** Data flows seamlessly from raw files to final visualizations without manual steps.
  
- **End-to-End Transparency:** Clear lineage from source data to dashboards.

- **Scalable Design:** Can handle batch or real-time (with future enhancements using Snowpipe or Kafka).

- **Domain Flexibility:** While demonstrated using hospital data, the architecture supports multi-domain use cases.



## 💬 **Use Cases**

While this example focuses on healthcare operational analytics, the same approach can be applied to:

- Retail sales and inventory analytics

- Logistics and supply chain performance monitoring

- Financial transaction and risk analytics

- Manufacturing production and quality monitoring



## 👨‍💻 **Author**

**Sumit Baviskar**  
📧 [Your Email]  
🔗 [LinkedIn](https://linkedin.com/in/your-profile)  
🔗 [Portfolio/GitHub](https://github.com/sumitbaviskar)
