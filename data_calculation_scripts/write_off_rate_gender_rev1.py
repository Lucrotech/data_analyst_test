import pandas as pd

# Load the cleaned_loans.csv and cleaned_borrowers.csv files
loans_file_path = "cleaned_loans.csv"       # Update with your file path
borrowers_file_path = "cleaned_borrowers.csv"  # Update with your file path

loans_df = pd.read_csv(loans_file_path, low_memory=False)
borrowers_df = pd.read_csv(borrowers_file_path, low_memory=False)

# Convert as_of_datetime and other relevant columns to datetime format
loans_df['as_of_datetime'] = pd.to_datetime(loans_df['as_of_datetime'], errors='coerce')
loans_df['maturity_date'] = pd.to_datetime(loans_df['maturity_date'], errors='coerce')
loans_df['issue_date'] = pd.to_datetime(loans_df['issue_date'], errors='coerce')

# Filter the loans DataFrame to only include rows where both loan_id and borrower_id are present
loans_df = loans_df.dropna(subset=['loan_id', 'borrower_id'])

# For each loan_id and borrower_id, select the record with the latest as_of_datetime
latest_loans_df = loans_df.sort_values('as_of_datetime').groupby(['loan_id', 'borrower_id']).tail(1)

# Merge the latest loans DataFrame with borrowers to include gender
loans_with_gender_df = pd.merge(latest_loans_df, borrowers_df[['borrower_id', 'gender']], on='borrower_id', how='inner')

# Group by currency and gender, then calculate the total write_off_amount and total principal_amount
write_off_summary_by_currency_gender = loans_with_gender_df.groupby(['currency', 'gender']).agg(
    total_write_off_amount=('write_off_amount', 'sum'),
    total_principal_amount=('principal_amount', 'sum')
).reset_index()

# Calculate the write-off rate for each currency and gender
write_off_summary_by_currency_gender['write_off_rate'] = (
    (write_off_summary_by_currency_gender['total_write_off_amount'] / 
     write_off_summary_by_currency_gender['total_principal_amount']) * 100
)

# Display the write-off rate by currency and gender
print("Write-off Rate by Currency and Gender:")
print(write_off_summary_by_currency_gender[['currency', 'gender', 'write_off_rate']])