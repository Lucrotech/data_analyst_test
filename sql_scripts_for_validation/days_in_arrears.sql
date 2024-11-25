-- Calculate the average loan period
SELECT AVG(DATEDIFF(day, issue_date, maturity_date)) AS average_loan_period
FROM loans
WHERE issue_date IS NOT NULL AND maturity_date IS NOT NULL;

-- Calculate average days between default_date and maturity_date for rows with a default_date
SELECT AVG(DATEDIFF(day, default_date, maturity_date)) AS average_days_default_to_maturity
FROM loans
WHERE default_date IS NOT NULL AND maturity_date IS NOT NULL;

-- Calculate average days between write_off_date and default_date for rows with both dates
SELECT AVG(DATEDIFF(day, default_date, write_off_date)) AS average_days_write_off_to_default
FROM loans
WHERE default_date IS NOT NULL AND write_off_date IS NOT NULL;