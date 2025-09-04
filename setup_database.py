import pandas as pd
import sqlite3
import os

# Connect to SQLite database
conn = sqlite3.connect('vaers.db')
data_dir = "data"
years = range(1990, 2026)

# Load VAERSDATA (main reports)
data_frames = []
for year in years:
    csv_path = os.path.join(data_dir, f"{year}VAERSDATA.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path, low_memory=False, encoding='ISO-8859-1')
        data_frames.append(df)
if data_frames:
    all_data = pd.concat(data_frames, ignore_index=True)
    all_data.to_sql('reports', conn, if_exists='replace', index=False)
    print("Loaded reports table.")

# Load VAERSSYMPTOMS
sym_frames = []
for year in years:
    csv_path = os.path.join(data_dir, f"{year}VAERSSYMPTOMS.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path, low_memory=False, encoding='ISO-8859-1')
        sym_frames.append(df)
if sym_frames:
    all_sym = pd.concat(sym_frames, ignore_index=True)
    all_sym.to_sql('symptoms', conn, if_exists='replace', index=False)
    print("Loaded symptoms table.")

# Load VAERSVAX
vax_frames = []
for year in years:
    csv_path = os.path.join(data_dir, f"{year}VAERSVAX.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path, low_memory=False, encoding='ISO-8859-1')
        vax_frames.append(df)
if vax_frames:
    all_vax = pd.concat(vax_frames, ignore_index=True)
    all_vax.to_sql('vaccines', conn, if_exists='replace', index=False)
    print("Loaded vaccines table.")

conn.close()
print("Database setup complete.")
