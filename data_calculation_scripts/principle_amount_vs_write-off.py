import pandas as pd
import matplotlib.pyplot as plt

def visualize_loans_data(file_path):
    """
    Visualizes the number of loans per month, total principal value, write-off date, and write-off value
    from the loans.csv file.

    Parameters:
        file_path (str): Path to the loans.csv file.

    Returns:
        None
    """
    try:
        # Load the data
        data = pd.read_csv(file_path)

        # Ensure date columns are properly parsed
        if "issue_date" in data.columns:
            data['issue_date'] = pd.to_datetime(data['issue_date'])
        if "write_off_date" in data.columns:
            data['write_off_date'] = pd.to_datetime(data['write_off_date'])

        # Extract loan month and year
        data['loan_month'] = data['issue_date'].dt.to_period('M')
        
        # Group by month for loans count and principal value
        monthly_data = data.groupby('loan_month').agg(
            number_of_loans=('loan_id', 'count'),
            total_principal_value=('principal_amount', 'sum')
        ).reset_index()
        
        # Plot: Number of loans per month
        plt.figure(figsize=(10, 6))
        plt.bar(monthly_data['loan_month'].astype(str), monthly_data['number_of_loans'], color='skyblue')
        plt.title('Number of Loans Per Month', fontsize=14)
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Number of Loans', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('loans_per_month.png')
        plt.show()

        # Plot: Total principal value per month
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_data['loan_month'].astype(str), monthly_data['total_principal_value'], marker='o', color='orange')
        plt.title('Total Principal Value Per Month', fontsize=14)
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Total Principal Value', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('principal_value_per_month.png')
        plt.show()

        # Handle write-off dates and values
        if 'write_off_date' in data.columns and 'write_off_value' in data.columns:
            write_off_data = data.groupby('write_off_date').agg(
                total_write_off_value=('write_off_value', 'sum')
            ).reset_index()

            # Plot: Total write-off value by date
            plt.figure(figsize=(10, 6))
            plt.bar(write_off_data['write_off_date'].astype(str), write_off_data['total_write_off_value'], color='red')
            plt.title('Total Write-Off Value by Date', fontsize=14)
            plt.xlabel('Write-Off Date', fontsize=12)
            plt.ylabel('Write-Off Value', fontsize=12)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('write_off_value_by_date.png')
            plt.show()

        print("Visualizations created and saved as PNG files in the current directory.")

    except Exception as e:
        print(f"Error processing the file: {e}")

# Path to the loans.csv file
file_path = "loans.csv"

# Run the function
visualize_loans_data(file_path)
