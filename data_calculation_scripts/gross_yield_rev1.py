import pandas as pd

# Load the cleaned_payments.csv and cleaned_loans.csv files
payments_file = "cleaned_payments.csv"  # Update with your file path
loans_file = "cleaned_loans.csv"        # Update with your file path

# Load only necessary columns
payments_df = pd.read_csv(payments_file, usecols=['loan_id', 'amount'])
loans_df = pd.read_csv(loans_file, usecols=['loan_id', 'principal_amount', 'currency'])

# Calculate total payments per loan_id
total_payments_per_loan = payments_df.groupby('loan_id').agg(
    total_collected_amount=('amount', 'sum')
).reset_index()

# Merge loans_df with payments data to get total collected amounts
loans_payments_df = pd.merge(loans_df, total_payments_per_loan, on='loan_id', how='left')
loans_payments_df['total_collected_amount'] = loans_payments_df['total_collected_amount'].fillna(0)

# Use total collected amount as total income
loans_payments_df['total_income'] = loans_payments_df['total_collected_amount']

# Group by 'currency' to calculate the components of the total income and principal amounts
currency_components = loans_payments_df.groupby('currency').agg(
    total_collected_amount=('total_collected_amount', 'sum'),
    total_income=('total_income', 'sum'),
    total_principal_amount=('principal_amount', 'sum')
).reset_index()

# Calculate the Gross Yield per currency as a percentage
currency_components['gross_yield'] = (
    (currency_components['total_income'] / currency_components['total_principal_amount']) * 100
)

# Display the result
print("\nComponents and Gross Yield Summary by Currency:")
print(currency_components)