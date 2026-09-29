import logging

logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    logger.debug("DataFrame shape: %s", df.shape)
    print("Shape:", df.shape)
    print("First five rows:")
    print(df.head())
    print("Column names:")
    print(df.columns)
    print("Data types:")
    print(df.dtypes)


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    before = len(df)
    result = df.drop_duplicates()
    logger.debug("Removed duplicates: %d rows before, %d rows after", before, len(result))
    return result


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    before_count = len(df)
    result = df.dropna()
    logger.debug("Dropped missing rows: %d -> %d", before_count, len(result))
    return result
