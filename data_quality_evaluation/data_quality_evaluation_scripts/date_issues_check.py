import pandas as pd

# Load the cleaned_loans.csv file
loans_file_path = "cleaned_loans.csv"  # Update with your file path
loans_df = pd.read_csv(loans_file_path, low_memory=False)

# Convert relevant columns to datetime format
loans_df['default_date'] = pd.to_datetime(loans_df['default_date'], errors='coerce')
loans_df['maturity_date'] = pd.to_datetime(loans_df['maturity_date'], errors='coerce')
loans_df['write_off_date'] = pd.to_datetime(loans_df['write_off_date'], errors='coerce')

# Filter rows where the default_date is before the maturity_date
defaults_before_maturity = loans_df[loans_df['default_date'] < loans_df['maturity_date']]

# Further filter where write_off_date is before default_date
write_off_before_default = defaults_before_maturity[defaults_before_maturity['write_off_date'] < defaults_before_maturity['default_date']]

# Display the top 50 examples
top_50_examples = write_off_before_default.head(50)

# Print the result
print("Top 50 examples where 'default_date' is before 'maturity_date' and 'write_off_date' is before 'default_date':")
print(top_50_examples)

# Save the result to a CSV file
output_file_path = "top_50_examples.csv"  # Update with your desired output file path
top_50_examples.to_csv(output_file_path, index=False)
print(f"Results saved to {output_file_path}")