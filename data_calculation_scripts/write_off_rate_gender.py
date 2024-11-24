import pandas as pd

def optimize_data_types(df):
    # Convert object types to category if they have a small number of unique values
    for col in df.select_dtypes(include='object').columns:
        num_unique_values = len(df[col].unique())
        num_total_values = len(df[col])
        if num_unique_values / num_total_values < 0.5:
            df[col] = df[col].astype('category')
    
    # Convert integer columns to the smallest possible integer type
    for col in df.select_dtypes(include='integer').columns:
        df[col] = pd.to_numeric(df[col], downcast='integer')
    
    # Convert float columns to the smallest possible float type
    for col in df.select_dtypes(include='float').columns:
        df[col] = pd.to_numeric(df[col], downcast='float')
    
    return df

# Load the cleaned_loans.csv and cleaned_borrowers.csv files
loans_file_path = "cleaned_loans.csv"  # Update with your file path
borrowers_file_path = "cleaned_borrowers.csv"  # Update with your file path

loans_df = pd.read_csv(loans_file_path, low_memory=False)
borrowers_df = pd.read_csv(borrowers_file_path, low_memory=False)

# Optimize data types
loans_df = optimize_data_types(loans_df)
borrowers_df = optimize_data_types(borrowers_df)

# Display the column names for debugging
print("Loans DataFrame columns:", loans_df.columns.tolist())
print("Borrowers DataFrame columns:", borrowers_df.columns.tolist())

# Merge the loans and borrowers DataFrames on 'borrower_id'
# Note: We are not dropping NaN values in the merged_df to avoid memory issues
merged_df = pd.merge(loans_df, borrowers_df[['borrower_id', 'gender']], on='borrower_id', how='inner', copy=False)

# Group by 'currency' and calculate the sum of 'write_off_amount' and 'principal_amount'
write_off_summary_currency = merged_df.groupby('currency', as_index=False).agg(
    total_write_off_amount=('write_off_amount', 'sum'),
    total_principal_amount=('principal_amount', 'sum')
)

# Calculate the Write-off Rate as a percentage for each currency
write_off_summary_currency['write_off_rate'] = (
    (write_off_summary_currency['total_write_off_amount'] / write_off_summary_currency['total_principal_amount']) * 100
)

# Display the original result by currency
print("Write-off Summary by Currency:")
print(write_off_summary_currency)

# New logic: Group by 'currency' and 'gender' to calculate the sum of 'write_off_amount' and 'principal_amount'
write_off_summary_currency_gender = merged_df.groupby(['currency', 'gender'], as_index=False).agg(
    total_write_off_amount=('write_off_amount', 'sum'),
    total_principal_amount=('principal_amount', 'sum')
)

# Calculate the Write-off Rate as a percentage for each currency and gender
write_off_summary_currency_gender['write_off_rate'] = (
    (write_off_summary_currency_gender['total_write_off_amount'] / write_off_summary_currency_gender['total_principal_amount']) * 100
)

# Display the new result by currency and gender
print("\nWrite-off Summary by Currency and Gender:")
print(write_off_summary_currency_gender)