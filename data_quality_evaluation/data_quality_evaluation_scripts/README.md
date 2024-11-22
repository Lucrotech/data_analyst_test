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