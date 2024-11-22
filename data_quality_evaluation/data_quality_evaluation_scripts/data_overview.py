import pandas as pd
import os

def export_random_sample(file_path, output_path, sample_size=20):
    """
    Exports a random sample of rows from a CSV file (including the header) to a new CSV file.

    Parameters:
        file_path (str): Path to the input CSV file.
        output_path (str): Path to save the sampled CSV file.
        sample_size (int): Number of random rows to sample.

    Returns:
        None
    """
    try:
        # Load the data
        data = pd.read_csv(file_path)

        # Check if the file has enough rows for the sample
        sample_size = min(sample_size, len(data))

        # Randomly sample rows
        sample_data = data.sample(n=sample_size, random_state=42)

        # Export the sampled data to a new CSV file
        sample_data.to_csv(output_path, index=False)

        print(f"Random sample of {sample_size} records exported to {output_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# List of files to process
files = [
    ("borrowers.csv", "borrowers_sample.csv"),
    ("loans.csv", "loans_sample.csv"),
    ("payments.csv", "payments_sample.csv")
]

# Process each file
for input_file, output_file in files:
    export_random_sample(input_file, output_file, sample_size=20)
