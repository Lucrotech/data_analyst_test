# DATA_ANALYST_TAKEHOME_TEST

This repository contains a structured set of scripts, data, and documentation designed to facilitate data analysis tasks related to loan processing and evaluation. Below is a description of the directory structure and contents.

## Directory Structure

### 1. `data_calculation_scripts`
This folder contains Python scripts used for performing various calculations related to loan data analysis. The scripts are designed to compute specific metrics and insights from the loan datasets.

- **`collection_rate.py`**: Computes the collection rate for loans.
- **`collection_rate_gender.py`**: Calculates collection rates segmented by gender.
- **`days_in_arrears.py`**: Analyzes the average days loans are in arrears.
- **`gross_yield.py`**: Calculates the gross yield for loans.
- **`write_off_rate.py`**: Determines the write-off rate for the loan portfolio.
- **`write_off_rate_gender.py`**: Analyzes write-off rates by gender.
- **`principle_amount_vs_write_off.py`**: Compares principal amounts against write-off amounts.

### 2. `data_processing_scripts`
This folder includes scripts for processing and cleaning loan and borrower data. These scripts prepare the data for analysis by handling missing values and ensuring consistency.

- **`combine_borrowers_loans.py`**: Merges borrower and loan datasets.
- **`combine_loans_payments.py`**: Integrates loan and payment data.
- **`remove_missing_borrowers.py`**: Cleans the dataset by removing records with missing borrower information.
- **`remove_missing_loan_id.py`**: Excludes entries with missing loan IDs.
- **`remove_missing_loans.py`**: Deletes records with incomplete loan data.

### 3. `findings_presentation`
This directory contains presentation materials summarizing the findings and analysis of the loan data.

- **`20241124_Swift_Loan_Data_Review_rev1.pdf`**: A PDF presentation providing an overview of the data analysis findings and recommendations.

### 4. `processed_data`
This folder holds the cleaned and processed datasets, ready for analysis locally and in the related AWS S3 bucket. Due to the size they were excluded from the GitHub repo (see gitignore for exclusions).

- **`cleaned_borrowers.csv`**: A CSV file containing cleaned borrower data.
- **`cleaned_loans.csv`**: A CSV file with cleaned loan information.
- **`cleaned_payments.csv`**: A CSV file of processed payment records.

### 5. `raw_data`
This directory contains the original, unprocessed data files locally and in the related AWS S3 bucket. Due to the size they were excluded from the GitHub repo (see gitignore for exclusions).

- **`borrowers.csv`**: The raw borrower dataset.
- **`loans.csv`**: The initial loan data file.
- **`payments.csv`**: The original payments dataset.

### 6. `task_and_data_dictionary`
This folder includes documentation and resources related to the task and data.

- **`Data analyst take home test.docx`**: A document detailing the task and requirements.
- **`Data Dictionary.xlsx`**: An Excel file containing descriptions and definitions of the dataset fields.

### `.gitignore`
This file specifies files and directories that should be ignored by version control, ensuring unnecessary files are not tracked in the repository.

---

This repository is organized to provide a comprehensive insight into how I analyzed the provided loan data, from data processing and cleaning to performing complex calculations and presenting findings. Each script and dataset serves a specific purpose in the analysis pipeline.