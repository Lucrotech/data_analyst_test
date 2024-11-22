import pandas as pd
import os

def analyze_data_quality(file_path, output_path):
    """
    Analyzes the quality of data in a CSV file and writes the output to a text file.

    Parameters:
        file_path (str): Path to the CSV file.
        output_path (str): Path to save the analysis results.

    Returns:
        None
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        with open(output_path, "w") as f:
            f.write(f"Error loading CSV file: {e}")
        return

    with open(output_path, "w") as f:
        f.write("\n--- Data Quality Analysis ---\n")
        f.write(f"File: {file_path}\n\n")

        # Basic information about the dataset
        f.write("1. Dataset Overview:\n")
        f.write(f"Number of rows: {data.shape[0]}\n")
        f.write(f"Number of columns: {data.shape[1]}\n\n")

        # Check for missing values
        f.write("2. Missing Values:\n")
        missing_values = data.isnull().sum()
        missing_summary = missing_values[missing_values > 0]
        if not missing_summary.empty:
            f.write(f"{missing_summary}\n")
        else:
            f.write("No missing values found.\n")
        f.write("\n")

        # Check for duplicate rows
        f.write("3. Duplicate Rows:\n")
        duplicate_count = data.duplicated().sum()
        f.write(f"Number of duplicate rows: {duplicate_count}\n\n")

        # Data types and invalid entries
        f.write("4. Data Types and Inconsistencies:\n")
        f.write(f"{data.dtypes}\n\n")

        # Descriptive statistics for numerical columns
        f.write("5. Descriptive Statistics (Numerical Columns):\n")
        f.write(f"{data.describe().T}\n\n")

        # Descriptive statistics for categorical columns
        f.write("6. Unique Values in Categorical Columns:\n")
        categorical_columns = data.select_dtypes(include=["object"]).columns
        for col in categorical_columns:
            f.write(f"{col}: {data[col].nunique()} unique values\n")

        f.write("\n--- End of Analysis ---\n")

# Define the file names
files = ["payments.csv", "borrowers.csv", "loans.csv"]

# Analyze each file
for file_name in files:
    file_path = file_name
    output_path = file_name.replace(".csv", "_analysis.txt")
    analyze_data_quality(file_path, output_path)

print("Data quality analysis completed. Results saved to text files.")
