import pandas as pd

# Load the cleaned_loans.csv file
loans_file_path = "cleaned_loans.csv"  # Update with your file path
loans_df = pd.read_csv(loans_file_path, low_memory=False)

# Convert relevant columns to datetime format
loans_df['maturity_date'] = pd.to_datetime(loans_df['maturity_date'], errors='coerce')
loans_df['default_date'] = pd.to_datetime(loans_df['default_date'], errors='coerce')
loans_df['write_off_date'] = pd.to_datetime(loans_df['write_off_date'], errors='coerce')

# Filter loans with maturity_date on or before 31 July 2024
eligible_loans_df = loans_df[loans_df['maturity_date'] <= pd.Timestamp('2024-07-31')]
total_eligible_loans = eligible_loans_df['loan_id'].nunique()
defaulted_eligible_loans = eligible_loans_df['default_date'].notna().sum()
default_percentage_eligible = (defaulted_eligible_loans / total_eligible_loans) * 100 if total_eligible_loans > 0 else 0
written_off_eligible_loans = eligible_loans_df['write_off_date'].notna().sum()
write_off_percentage_eligible = (written_off_eligible_loans / total_eligible_loans) * 100 if total_eligible_loans > 0 else 0

# Calculate the total number of loans
total_loans = loans_df['loan_id'].nunique()

# Filter loans with a write_off_date after 31 July 2024
loans_written_off_after_july = loans_df[loans_df['write_off_date'] > pd.Timestamp('2024-07-31')]
written_off_loans_after_july = loans_written_off_after_july['loan_id'].nunique()
write_off_percentage_after_july = (written_off_loans_after_july / total_loans) * 100 if total_loans > 0 else 0

# Filter loans with a default_date after 31 July 2024
loans_defaulted_after_july = loans_df[loans_df['default_date'] > pd.Timestamp('2024-07-31')]
defaulted_loans_after_july = loans_defaulted_after_july['loan_id'].nunique()
default_percentage_after_july = (defaulted_loans_after_july / total_loans) * 100 if total_loans > 0 else 0

# Display the results
print(f"Percentage of Eligible Loans that Default (maturity on or before 31 July 2024): {default_percentage_eligible:.2f}%")
print(f"Percentage of Eligible Loans that were Written Off (maturity on or before 31 July 2024): {write_off_percentage_eligible:.2f}%")
print(f"Percentage of Loans that were Written Off After 31 July 2024: {write_off_percentage_after_july:.2f}%")
print(f"Percentage of Loans that Defaulted After 31 July 2024: {default_percentage_after_july:.2f}%")