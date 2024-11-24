import pandas as pd

# Load the cleaned_payments.csv file
file_path = "cleaned_payments.csv"  # Update with your file path
payments_df = pd.read_csv(file_path)

# Ensure the payment_date column is in datetime format
payments_df['payment_date'] = pd.to_datetime(payments_df['payment_date'])

# Group by 'currency' and get the maximum 'payment_date' for each group
last_payment_dates = payments_df.groupby('currency')['payment_date'].max().reset_index()

# Rename the columns for clarity
last_payment_dates.columns = ['currency', 'last_payment_date']

# Display the result
print(last_payment_dates)
