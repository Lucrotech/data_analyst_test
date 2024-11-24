import pandas as pd

# Load the cleaned_loans.csv file
loans_file_path = "cleaned_loans.csv"  # Update with your file path
loans_df = pd.read_csv(loans_file_path, low_memory=False)

# Convert relevant columns to datetime format
loans_df['issue_date'] = pd.to_datetime(loans_df['issue_date'], errors='coerce')
loans_df['maturity_date'] = pd.to_datetime(loans_df['maturity_date'], errors='coerce')
loans_df['default_date'] = pd.to_datetime(loans_df['default_date'], errors='coerce')
loans_df['write_off_date'] = pd.to_datetime(loans_df['write_off_date'], errors='coerce')

# Calculate the average loan period (maturity_date - issue_date)
loans_df['loan_period_days'] = (loans_df['maturity_date'] - loans_df['issue_date']).dt.days
average_loan_period = loans_df['loan_period_days'].mean()

# Calculate average days between default_date and maturity_date for rows with a default_date
loans_with_default = loans_df.dropna(subset=['default_date'])
loans_with_default['days_default_to_maturity'] = (loans_with_default['maturity_date'] - loans_with_default['default_date']).dt.days
average_days_default_to_maturity = loans_with_default['days_default_to_maturity'].mean()

# Calculate average days between write_off_date and default_date for rows with both dates
loans_with_write_off = loans_with_default.dropna(subset=['write_off_date'])
loans_with_write_off['days_write_off_to_default'] = (loans_with_write_off['write_off_date'] - loans_with_write_off['default_date']).dt.days
average_days_write_off_to_default = loans_with_write_off['days_write_off_to_default'].mean()

# Display the results
print(f"Average Loan Period (days): {average_loan_period:.2f}")
print(f"Average Days Between Default and Maturity (for loans with defaults): {average_days_default_to_maturity:.2f}")
print(f"Average Days Between Write-off and Default (for loans with defaults and write-offs): {average_days_write_off_to_default:.2f}")