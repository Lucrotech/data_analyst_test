import pandas as pd

# Load the loans.csv file
loans_file_path = "cleaned_loans.csv"  # Update with your file path
loans_df = pd.read_csv(loans_file_path, low_memory=False)

# Convert relevant columns to datetime format
loans_df['maturity_date'] = pd.to_datetime(loans_df['maturity_date'], errors='coerce')

# Filter loans with a maturity_date on or before 31 July 2024
filtered_loans_df = loans_df[loans_df['maturity_date'] <= pd.Timestamp('2024-07-31')]

# Group by currency and calculate the total write_off_amount and total principal_amount for each currency
write_off_summary_by_currency = filtered_loans_df.groupby('currency').agg(
    total_write_off_amount=('write_off_amount', 'sum'),
    total_principal_amount=('principal_amount', 'sum')
).reset_index()

# Calculate the write-off rate for each currency
write_off_summary_by_currency['write_off_rate'] = (
    (write_off_summary_by_currency['total_write_off_amount'] / write_off_summary_by_currency['total_principal_amount']) * 100
)

# Display the write-off rate by currency
print("Write-off Rate by Currency for loans maturing on or before 31 July 2024:")
print(write_off_summary_by_currency[['currency', 'write_off_rate']])