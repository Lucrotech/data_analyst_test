# Data Quality Analysis Script

## Overview
This script, `data_quality_analysis.py`, is designed to evaluate the quality of datasets stored in CSV format. It provides a detailed analysis of key data quality aspects, including missing values, duplicate rows, data types, and descriptive statistics. The results are saved to text files for easy review and documentation.

## Features
- **Dataset Overview**: Summarizes the number of rows and columns in the dataset.
- **Missing Value Analysis**: Identifies columns with missing data and reports their counts.
- **Duplicate Rows Check**: Counts the number of duplicate rows in the dataset.
- **Data Type Validation**: Lists data types of all columns and identifies potential inconsistencies.
- **Descriptive Statistics**:
  - Numerical columns: Basic statistics (mean, min, max, etc.).
  - Categorical columns: Number of unique values.
- **Scalability**: Analyzes multiple datasets in a single run.

## Requirements
- Python 3.7+
- Pandas library

Install Pandas with:
```bash
pip install pandas

Usage
Prepare Your CSV Files: Ensure your CSV files are in the same directory as the script or provide their file paths.
Run the Script: Execute the script using a Python interpreter:
bash
Copy code
python data_quality_analysis.py
Check the Output: The analysis results will be saved as text files in the same directory as the input files, with the naming convention <filename>_analysis.txt.
Input Files
The script is currently configured to analyze the following files:

payments.csv
borrowers.csv
loans.csv
You can modify the files list in the script to include additional file names or paths.

Output Files
For each input file, a corresponding output file will be generated with a detailed quality analysis. Example:

Input: payments.csv
Output: payments_analysis.txt
Customization
To customize the script:

File Paths: Update the files list with your dataset file names or paths.
Analysis Scope: Modify the analyze_data_quality function to add/remove specific checks.
Error Handling
The script checks if the specified files exist before processing.
If an error occurs while loading a CSV file, the script writes the error details to the output file.