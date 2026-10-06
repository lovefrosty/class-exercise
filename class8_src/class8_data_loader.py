import logging
import pandas as pd

logger = logging.getLogger(__name__)

def load_netflix(filepath):
    """Load the Netflix CSV file."""
    df = pd.read_csv(filepath)
    logger.info("Loaded Netflix data from %s", filepath)
    return df
