import requests
import zipfile
import os

# Create data folder
os.makedirs("data", exist_ok=True)

# Years to download (1990–2025)
years = range(1990, 2026)
base_url = "https://vaers.hhs.gov/eSubDownload/index.jsp?fn="

for year in years:
    zip_filename = f"{year}VAERSData.zip"
    zip_path = os.path.join("data", zip_filename)
    
    print(f"Downloading {zip_filename}...")
    response = requests.get(base_url + zip_filename, stream=True)
    if response.status_code == 200:
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        print(f"Failed to download {year}")
        continue
    
    # Extract ZIP
    print(f"Extracting {zip_filename}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("data")
    
    # Delete ZIP to save space
    os.remove(zip_path)

print("All downloads and extractions complete.")
