

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Helper function
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

departments = ['Emergency', 'ICU', 'General Surgery', 'Orthopedics', 'Cardiology', 'Neurology', 'Pediatrics']
bed_statuses = ['Available', 'Occupied', 'Under Maintenance']
admission_types = ['Emergency', 'Elective', 'Transfer']
discharge_statuses = ['Recovered', 'Deceased', 'Transferred']
discharge_destinations = ['Home', 'Rehab', 'Another hospital']
genders = ['M', 'F', 'Other']
insurance_types = ['Private', 'Public', 'Self-pay']
bed_types = ['ICU', 'General', 'Isolation', 'Pediatric']

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 6, 30)

# 1️⃣ admissions.csv
admissions = []
for i in range(200000):
    patient_id = f"P{i+1:05}"
    admission_id = f"A{i+1:05}"
    admit_time = random_date(start_date, end_date)
    department = random.choice(departments)
    bed_id = f"B{random.randint(1, 500):04}"
    admission_type = random.choice(admission_types)
    age = random.randint(1, 95)
    gender = random.choice(genders)
    primary_diagnosis = random.choice(['Infection', 'Fracture', 'Heart Attack', 'Stroke', 'Routine Check', 'Surgery'])
    insurance_type = random.choice(insurance_types)
    admissions.append([patient_id, admission_id, admit_time, department, bed_id, admission_type, age, gender, primary_diagnosis, insurance_type])

df_admissions = pd.DataFrame(admissions, columns=['patient_id', 'admission_id', 'admit_time', 'department', 'bed_id', 'admission_type', 'age', 'gender', 'primary_diagnosis', 'insurance_type'])

# 2️⃣ discharges.csv
discharges = []
for i in range(200000):
    patient_id = f"P{i+1:05}"
    admission_id = f"A{i+1:05}"
    discharge_time = random_date(start_date, end_date + timedelta(days=30))
    discharge_status = random.choice(discharge_statuses)
    department = random.choice(departments)
    length_of_stay = random.randint(1, 30)
    discharge_destination = random.choice(discharge_destinations)
    discharges.append([patient_id, admission_id, discharge_time, discharge_status, department, length_of_stay, discharge_destination])

df_discharges = pd.DataFrame(discharges, columns=['patient_id', 'admission_id', 'discharge_time', 'discharge_status', 'department', 'length_of_stay', 'discharge_destination'])

# 3️⃣ transfers.csv
transfers = []
for i in range(200000):
    patient_id = f"P{random.randint(1, 3000):05}"
    admission_id = f"A{random.randint(1, 3000):05}"
    transfer_time = random_date(start_date, end_date)
    from_department = random.choice(departments)
    to_department = random.choice([d for d in departments if d != from_department])
    reason = random.choice(['Condition worsened', 'Specialist treatment', 'Bed availability', 'Post-op care'])
    transfers.append([patient_id, admission_id, transfer_time, from_department, to_department, reason])

df_transfers = pd.DataFrame(transfers, columns=['patient_id', 'admission_id', 'transfer_time', 'from_department', 'to_department', 'reason'])

# 4️⃣ bed_inventory.csv
bed_inventory = []
for i in range(200000):
    bed_id = f"B{i+1:04}"
    department = random.choice(departments)
    bed_status = random.choice(bed_statuses)
    last_updated = random_date(start_date, end_date)
    room_number = f"R{random.randint(1, 200):03}"
    bed_type = random.choice(bed_types)
    is_critical_care = random.choice([True, False])
    bed_inventory.append([bed_id, department, bed_status, last_updated, room_number, bed_type, is_critical_care])

df_bed_inventory = pd.DataFrame(bed_inventory, columns=['bed_id', 'department', 'bed_status', 'last_updated', 'room_number', 'bed_type', 'is_critical_care'])

df_admissions.head()

# prompt: download

from google.colab import files

# Download the generated CSV files
df_admissions.to_csv('admissions.csv', index=False)
files.download('admissions.csv')

df_discharges.head()

df_discharges.to_csv('discharges.csv', index=False)
files.download('discharges.csv')

df_transfers.head()

df_transfers.to_csv('transfers.csv', index=False)
files.download('transfers.csv')

df_bed_inventory.head()

df_bed_inventory.to_csv('bed_inventory.csv', index=False)
files.download('bed_inventory.csv')


