import json
import logging
from pathlib import Path

import pandas as pd
import yaml
import os
from dotenv import load_dotenv


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def inspect_csv(filepath):
    """Read a CSV file and display basic information."""
    # TODO:
    # 1. Read the file using pd.read_csv().
    # 2. Log the filepath at INFO.
    # 3. Print the first three rows (e.g. DataFrame.head(3))
    
    df = pd.read_csv(filepath)
    
    logger.info("Reading the CSV file: %s", filepath)
    
    return print(df.head(3))

    

def inspect_json(filepath):
    """Read a JSON file and display basic information."""
    # TODO:
    # 1. Open the file and read it using json.load().
    # 2. Log the filepath at INFO.
    # 3. Print the contents.
    
    with open(filepath, "r") as f:
        data = json.load(f)
        

        logger.info("Reading the json file: %s", filepath)
    
    return print(data)



def inspect_yaml(filepath):
    """Read a YAML file and display basic information."""
    # TODO:
    # 1. Open the file and read it using yaml.safe_load().
    # 2. Log the filepath at INFO.
    # 3. Print the contents.
    
    with open(filepath, "r") as f:
        config = yaml.safe_load(f)

    logger.info("Reading the YAML file: %s", filepath)

    return print(config["cleaning"]["missing"], config["processing"]["batch_size"])



def inspect_env():
    """Read a .env file and display basic information."""
    load_dotenv()

    keys = [
        key for key in ["USERNAME", "PASSWORD"]
        if os.getenv(key) is not None
    ]

    # TODO:
    # 1. Log at INFO that .env was loaded.
    # 2. Print keys.
    # Do not print passwords, API keys, or other secret values.

    logger.info("env was loaded")
    
    return print(keys)


def main():
    data_dir = Path(__file__).parent / "data"
    inspect_csv(data_dir / "sample.csv")
    inspect_json(data_dir / "sample.json")
    inspect_yaml(data_dir / "sample.yaml")
    inspect_env()


if __name__ == "__main__":
    main()
