import pandas as pd

# Load the cleaned_payments.csv and cleaned_loans.csv files
payments_file = "cleaned_payments.csv"  # Update with your file path
loans_file = "cleaned_loans.csv"        # Update with your file path

payments_df = pd.read_csv(payments_file)
loans_df = pd.read_csv(loans_file)

# Convert 'maturity_date' to datetime format
loans_df['maturity_date'] = pd.to_datetime(loans_df['maturity_date'], errors='coerce')

# Filter loans with maturity_date up to 31 July 2024
filtered_loans_df = loans_df[loans_df['maturity_date'] <= pd.Timestamp('2024-07-31')]

# Group by 'currency' to calculate the sum of 'amount' in cleaned_payments.csv
payments_summary = payments_df.groupby('currency').agg(
    total_collected_amount=('amount', 'sum')
).reset_index()

# Group by 'currency' to calculate the sum of 'principal_amount' in filtered_loans_df
loans_summary = filtered_loans_df.groupby('currency').agg(
    total_principal_amount=('principal_amount', 'sum')
).reset_index()

# Merge the payments summary with loans summary by currency
merged_summary = pd.merge(payments_summary, loans_summary, on='currency', how='inner')

# Calculate the Collections Rate as a percentage
merged_summary['collections_rate'] = (
    (merged_summary['total_collected_amount'] / merged_summary['total_principal_amount']) * 100
)

# Display the result
print("\nCollections Rate Summary by Currency (Maturity Date <= 31 July 2024):")
print(merged_summary)