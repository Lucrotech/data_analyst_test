import pandas as pd

# Load the cleaned_payments.csv and cleaned_loans.csv files
payments_file = "cleaned_payments.csv"  # Update with your file path
loans_file = "cleaned_loans.csv"        # Update with your file path

# Specify the dtype for the problematic column if known
# dtype_specification = {'column_name_placeholder': str}  # Replace 'column_name_placeholder' with the actual column name

payments_df = pd.read_csv(payments_file)
loans_df = pd.read_csv(loans_file, low_memory=False)

# Convert 'as_of_datetime' and 'payment_date' to datetime format
loans_df['as_of_datetime'] = pd.to_datetime(loans_df['as_of_datetime'], errors='coerce')
payments_df['payment_date'] = pd.to_datetime(payments_df['payment_date'], errors='coerce')

# Select the latest record per loan_id based on as_of_datetime
latest_loans_df = loans_df.loc[loans_df.groupby('loan_id')['as_of_datetime'].idxmax()]

# Calculate total payments per loan_id
total_payments_per_loan = payments_df.groupby('loan_id').agg(
    total_collected_amount=('amount', 'sum')
).reset_index()

# Merge with latest_loans_df to ensure we have all loans even if no payments have been made
loans_payments_df = pd.merge(latest_loans_df, total_payments_per_loan, on='loan_id', how='left')
loans_payments_df['total_collected_amount'] = loans_payments_df['total_collected_amount'].fillna(0)

# Filter loans with as_of_datetime up to 31 July 2024
filtered_loans_df = loans_payments_df[loans_payments_df['as_of_datetime'] <= pd.Timestamp('2024-07-31')]

# Group by 'currency' to calculate the total collected and principal amounts
currency_summary = filtered_loans_df.groupby('currency').agg(
    total_collected_amount=('total_collected_amount', 'sum'),
    total_principal_amount=('principal_amount', 'sum')
).reset_index()

# Calculate the Collections Rate per currency as a percentage
currency_summary['collections_rate'] = (
    (currency_summary['total_collected_amount'] / currency_summary['total_principal_amount']) * 100
)

# Calculate the total amount of issued loans and total amount of collected payments
total_issued_loans = loans_payments_df['principal_amount'].sum()
total_collected_payments = loans_payments_df['total_collected_amount'].sum()

# Display the results
print("\nCollections Rate Summary by Currency (as_of_datetime <= 31 July 2024):")
print(currency_summary)
print(f"\nTotal Amount of Issued Loans: {total_issued_loans:.2f}")
print(f"Total Amount of Payments Collected: {total_collected_payments:.2f}")