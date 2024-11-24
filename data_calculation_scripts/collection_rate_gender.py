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

# Load the cleaned_payments.csv, cleaned_loans.csv, and cleaned_borrowers.csv files
payments_file = "cleaned_payments.csv"  # Update with your file path
loans_file = "cleaned_loans.csv"        # Update with your file path
borrowers_file = "cleaned_borrowers.csv"  # Update with your file path

payments_df = pd.read_csv(payments_file, low_memory=False)
loans_df = pd.read_csv(loans_file, low_memory=False)
borrowers_df = pd.read_csv(borrowers_file, low_memory=False)

# Optimize data types
payments_df = optimize_data_types(payments_df)
loans_df = optimize_data_types(loans_df)
borrowers_df = optimize_data_types(borrowers_df)

# Convert 'maturity_date' to datetime format
loans_df['maturity_date'] = pd.to_datetime(loans_df['maturity_date'], errors='coerce')

# Filter loans with maturity_date up to 31 July 2024
filtered_loans_df = loans_df[loans_df['maturity_date'] <= pd.Timestamp('2024-07-31')]

# Merge filtered loans_df with borrowers_df to include 'gender'
loans_with_gender_df = pd.merge(filtered_loans_df, borrowers_df[['borrower_id', 'gender']], on='borrower_id', how='inner')

# Group by 'currency' to calculate the sum of 'amount' in cleaned_payments.csv
payments_summary = payments_df.groupby('currency').agg(
    total_collected_amount=('amount', 'sum')
).reset_index()

# Group by 'currency' and 'gender' to calculate the sum of 'principal_amount' in loans_with_gender_df
loans_summary_gender = loans_with_gender_df.groupby(['currency', 'gender']).agg(
    total_principal_amount=('principal_amount', 'sum')
).reset_index()

# Merge the payments summary with loans summary by currency and gender
merged_summary_gender = pd.merge(payments_summary, loans_summary_gender, on='currency', how='inner')

# Calculate the Collections Rate as a percentage for each currency and gender
merged_summary_gender['collections_rate'] = (
    (merged_summary_gender['total_collected_amount'] / merged_summary_gender['total_principal_amount']) * 100
)

# Display the result with gender
print("\nCollections Rate Summary by Currency and Gender (Maturity Date <= 31 July 2024):")
print(merged_summary_gender)