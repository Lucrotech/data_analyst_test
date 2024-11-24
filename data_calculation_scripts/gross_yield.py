import pandas as pd

# Load the cleaned_loans.csv file
loans_file_path = "cleaned_loans.csv"  # Update with your file path
loans_df = pd.read_csv(loans_file_path, low_memory=False)

# Explicitly convert relevant columns to datetime format
loans_df['issue_date'] = pd.to_datetime(loans_df['issue_date'], errors='coerce')
loans_df['maturity_date'] = pd.to_datetime(loans_df['maturity_date'], errors='coerce')

# Filter to only include loans with maturity_date of 31 July 2024 or earlier
loans_df = loans_df[loans_df['maturity_date'] <= pd.Timestamp('2024-07-31')]

# Calculate the loan period in days
loans_df['loan_period_days'] = (loans_df['maturity_date'] - loans_df['issue_date']).dt.days

# Calculate interest income for each loan
loans_df['interest_income'] = loans_df['principal_amount'] * loans_df['interest_rate'] * (loans_df['loan_period_days'] / 365)

# Load the cleaned_payments.csv file
payments_df = pd.read_csv("cleaned_payments.csv", parse_dates=['payment_date'])

# Sum payments related to each loan
payments_summary = payments_df.groupby('loan_id').agg(
    total_payments=('amount', 'sum')
).reset_index()

# Merge the payments summary with loans data
loans_with_payments = pd.merge(loans_df, payments_summary, on='loan_id', how='left')

# Fill NA values for total_payments with 0
loans_with_payments['total_payments'].fillna(0, inplace=True)

# Calculate total income
loans_with_payments['total_income'] = (loans_with_payments['interest_income'] + 
                                       loans_with_payments['penalties'] + 
                                       loans_with_payments['fees'] + 
                                       loans_with_payments['total_payments'])

# Calculate gross yield for each loan
loans_with_payments['gross_yield'] = (loans_with_payments['total_income'] / loans_with_payments['principal_amount']) * 100

# Calculate the average gross yield by currency
average_gross_yield_by_currency = loans_with_payments.groupby('currency').agg(
    average_gross_yield=('gross_yield', 'mean')
).reset_index()

# Display the results
print("Average Gross Yield by Currency:")
print(average_gross_yield_by_currency)