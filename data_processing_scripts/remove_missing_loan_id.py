import pandas as pd

def remove_missing_loan_id(input_file, output_file):
    """
    Remove rows where loan_id is missing from the payments CSV file.

    Parameters:
    input_file (str): The path to the input CSV file.
    output_file (str): The path to save the cleaned CSV file.
    """
    # Load the payments CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Display the number of rows before removing missing loan_id
    print(f"Number of rows before cleaning: {len(df)}")

    # Remove rows where loan_id is missing
    df_cleaned = df.dropna(subset=['loan_id'])

    # Display the number of rows after removing missing loan_id
    print(f"Number of rows after cleaning: {len(df_cleaned)}")

    # Save the cleaned DataFrame to a new CSV file
    df_cleaned.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Define the input and output file paths
    input_file_path = 'payments.csv'  # Update with the actual path
    output_file_path = 'cleaned_payments.csv'  # Update with the desired output path

    # Call the function to remove missing loan_id
    remove_missing_loan_id(input_file_path, output_file_path)