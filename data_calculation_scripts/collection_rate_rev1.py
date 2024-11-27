import pandas as pd

# Load the cleaned_payments.csv and cleaned_loans.csv files
payments_file = "cleaned_payments.csv"  # Update with your file path
loans_file = "cleaned_loans.csv"        # Update with your file path

payments_df = pd.read_csv(payments_file)
loans_df = pd.read_csv(loans_file)

# Convert 'as_of_datetime' to datetime format
loans_df['as_of_datetime'] = pd.to_datetime(loans_df['as_of_datetime'], errors='coerce')
payments_df['payment_date'] = pd.to_datetime(payments_df['payment_date'], errors='coerce')  # Assuming 'payment_date' exists

# Calculate total payments per loan_id
total_payments_per_loan = payments_df.groupby('loan_id').agg(
    total_collected_amount=('amount', 'sum')
).reset_index()

# Merge with loans_df to ensure we have all loans even if no payments have been made
loans_payments_df = pd.merge(loans_df, total_payments_per_loan, on='loan_id', how='left')
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

# Display the result
print("\nCollections Rate Summary by Currency (as_of_datetime <= 31 July 2024):")
print(currency_summary)