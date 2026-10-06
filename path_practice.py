from pathlib import Path
import logging 
import pandas as pd
import json
import yaml


# Clean object-oriented approach
data_dir = Path('data')
file_path = data_dir / 'sales.csv'  # Works everywhere!
# / is concatination on strings

# Check if exists
if file_path.exists():
    print("File exists")

# Get extension
ext = file_path.suffix  # '.csv'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# 1. Creating paths
file_path   = Path('data') / 'sales.csv'
config_path = Path('config') / 'settings.yaml'

# 2. Path properties
print(file_path.name)    # 'sales.csv'
print(file_path.stem)    # 'sales'
print(file_path.suffix)  # '.csv'
print(file_path.parent)  # 'data'

# 3. Checking existence — log the outcome
if not file_path.exists():
    logger.warning(f"File does not exist: {file_path}")
else:
    logger.info(f"File found: {file_path.name}")

# 4. Checking whether a path is specifically a file
if file_path.is_file():
    logger.info(f"{file_path.name} is a file")

#read csv
df = pd.read_csv("sample.csv")
print(df)

# read json
with open("sample.json", "r") as f:
    data = json.load(f)

print(data["status"])

'''

Example JSON
# sample.json
{"Status": "success",
"Count":3,
"Data":[{"name": "Alice", "city": "Boston"},
    {"name": "Bob", "city": "New York"},
    {"name": "Charlie", "city": "Chicago"}]
}

'''


# write json
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)

# YAML used for configuration files 

'''
Instead of using these configurations as variables in the program we can instead use 
YAML to house those configurations elsewhere
# sample.yaml
cleaning:
  missing: "drop"

processing:
  batch_size: 100

'''

# read YAML
with open("sample.yaml", "r") as f:
    config = yaml.safe_load(f)

print(config["cleaning"]["missing"])
print(config["processing"]["batch_size"])

# .env sensitive credentials in configuration

'''
Do not commit the .env to GitHub
# .env
USERNAME=ds3500demo
PASSWORD=ds3500
API_KEY=12345abcde

These are the API keys 


'''

# loading the enviroment variables in Python:
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
api_key = os.getenv("API_KEY")

print(password)
# Never print passwords, API keys, or other secrets in a real application.

