import pandas as pd

# Function to optimize data types without affecting datetime columns
def optimize_dataframe(df):
    # Convert object types to category, except datetime-like columns
    for col in df.select_dtypes(include=['object']).columns:
        if not pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].astype('category')
    # Optimize integers and floats
    for col in df.select_dtypes(include=['int', 'float']).columns:
        df[col] = pd.to_numeric(df[col], downcast='unsigned')
    return df

# Load the cleaned_payments.csv, cleaned_loans.csv, and cleaned_borrowers.csv files with necessary columns
payments_file = "cleaned_payments.csv"  # Update with your file path
loans_file = "cleaned_loans.csv"        # Update with your file path
borrowers_file = "cleaned_borrowers.csv"  # Update with your file path

# Load only necessary columns
payments_df = pd.read_csv(payments_file, usecols=['loan_id', 'amount', 'payment_date'])
loans_df = pd.read_csv(loans_file, usecols=['loan_id', 'borrower_id', 'principal_amount', 'currency', 'as_of_datetime'])
borrowers_df = pd.read_csv(borrowers_file, usecols=['borrower_id', 'gender'])

# Convert 'as_of_datetime' and 'payment_date' to datetime format
loans_df['as_of_datetime'] = pd.to_datetime(loans_df['as_of_datetime'], errors='coerce')
payments_df['payment_date'] = pd.to_datetime(payments_df['payment_date'], errors='coerce')  # Assuming 'payment_date' exists

# Optimize dataframes except for datetime columns
payments_df = optimize_dataframe(payments_df)
loans_df = optimize_dataframe(loans_df)
borrowers_df = optimize_dataframe(borrowers_df)

# Calculate total payments per loan_id
total_payments_per_loan = payments_df.groupby('loan_id', observed=True).agg(
    total_collected_amount=('amount', 'sum')
).reset_index()

# Merge loans_df with payments data
loans_payments_df = pd.merge(loans_df, total_payments_per_loan, on='loan_id', how='left')
loans_payments_df['total_collected_amount'] = loans_payments_df['total_collected_amount'].fillna(0)

# Merge loans_payments_df with borrowers_df to include gender information
loans_borrowers_df = pd.merge(loans_payments_df, borrowers_df, on='borrower_id', how='left')

# Filter loans with as_of_datetime up to 31 July 2024
filtered_loans_df = loans_borrowers_df[loans_borrowers_df['as_of_datetime'] <= pd.Timestamp('2024-07-31')]

# Group by 'currency' and 'gender' to calculate the total collected and principal amounts
currency_gender_summary = filtered_loans_df.groupby(['currency', 'gender'], observed=True).agg(
    total_collected_amount=('total_collected_amount', 'sum'),
    total_principal_amount=('principal_amount', 'sum')
).reset_index()

# Calculate the Collections Rate per currency and gender as a percentage
currency_gender_summary['collections_rate'] = (
    (currency_gender_summary['total_collected_amount'] / currency_gender_summary['total_principal_amount']) * 100
)

# Display the result
print("\nCollections Rate Summary by Currency and Gender (as_of_datetime <= 31 July 2024):")
print(currency_gender_summary)