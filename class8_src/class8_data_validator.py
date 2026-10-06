import logging

logger = logging.getLogger(__name__)

def required_cols(df, required_cols):
    """Check that all required columns exist."""
    missing_columns = [column for column in required_cols if column not in df.columns]
    if missing_columns:
        # logger.error("Missing required columns: %s", missing_columns)
        logger.error(f"Missing Columns: {",".join(missing_columns)}")

        raise ValueError(f"Missing required columns: {missing_columns}")
    logger.info("All required columns exist.")
    return df
