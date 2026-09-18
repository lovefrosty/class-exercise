import argparse

# This is what we have been doing! After today we are going to use
# the input data coming from the command line interface from the user.
# input_data = "sales.csv"
# pd.read_csv(input_data)

# Create an ArgumentPaser Object
parser = argparse.ArgumentParser(description="Analyze a data file")

parser.add_argument(
    "--input",
    "-i", # can use -i instead of --input 
    required=True,
    help="Path to input CSV file"
)

parser.add_argument("--output", 
    "-o", #stands for output, but is shorter
    # If the user doesn't use the python3 class2_argparse_demo.py -o option, the default value will be used
    default="results.txt",
    help="Output file path"
)

parser.add_argument("--verbose", 
    "-v",
    action="store_true",
    help="Enable verbose output"
)

args = parser.parse_args(
)