import argparse
import csv
import sys
from pathlib import Path
import logging


def check_data(filename):
    """Read the CSV file and check for missing values."""
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows[0]
    data = rows[1:]
    missing_rows = []

    for row_number, row in enumerate(data, start=2):
        if any(value == "" for value in row):
            missing_rows.append(row_number)

    return header, data, missing_rows


#step 1
# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)


#step 2
# Create a module-level logger
logger = logging.getLogger(__name__)


# TODO 1: Create an ArgumentParser
# Description: "Check the quality of a CSV file."
args = argparse.ArgumentParser(description="Check the quality of a CSV file.")


# TODO 2: Add a named argument (required):
# Long form: --input
# Short form: -i
# Help: "CSV file to check"
args.add_argument(
    "--input",
    "-i",
    required=True,
    help="CSV file to check"
)

# TODO 3: Add an named argument (optional):
# Long form: --output
# Short form: -o
# Default: "data_quality.txt"
# Help: "Output report filename"
args.add_argument(
    "--output",
    "-o",
    default="data_quality.txt",
    help="Output report filename"
)

# TODO 4: Add a boolean flag:
# Long form: --verbose
# Short form: -v
# Use action="store_true"
# Help: "Show detailed DEBUG messages"
args.add_argument(
    "--verbose",
    "-v",
    action="store_true",
    help="Show detailed DEBUG messages"
)


# TODO 5: Parse the command-line arguments
args = args.parse_args()

"""
control the logging level

Without --verbose -> show INFO and above
With --verbose -> show DEBUG and above
"""

#step 3
if args.verbose:
    logger.setLevel(logging.DEBUG)

logger.debug(f"Arguments passed: filename={args.input}'")


#Step 5
# Check if the file exists 
p = Path(args.input)
if not p.is_file():
    logger.error(f"File not found: '{args.input}'")
    sys.exit(1)
    
logger.info(f"File validated: '{args.input}'")

#Step 6
logger.debug(f"Loading data from: '{args.input}'")


# Check the data
header, data, missing_rows = check_data(args.input)

#step 7
logger.info(f"Number of columns: {len(data)}")

#step 8
if len(data) == 0:
    logger.error("Input file contains no data; cannot continue")
    sys.exit(1)

#step 9 
for row_number in missing_rows:
    logger.warning(f"Row {row_number} has missing values")
    

# Save the report
with open(args.output, "w") as f:
    f.write(f"Number of rows: {len(data)}\n")
    f.write(f"Number of columns: {len(header)}\n")
    f.write(f"Number of rows with missing values: {len(missing_rows)}\n")

#step 10
logger.info(f"Report saved to {args.output}'")