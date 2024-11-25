WITH filtered_loans AS (
    SELECT 
        currency, 
        write_off_amount, 
        principal_amount
    FROM 
        loans
    WHERE 
        maturity_date <= '2024-07-31'
)

SELECT 
    currency,
    SUM(write_off_amount) AS total_write_off_amount,
    SUM(principal_amount) AS total_principal_amount,
    (SUM(write_off_amount) / NULLIF(SUM(principal_amount), 0)) * 100 AS write_off_rate
FROM 
    filtered_loans
GROUP BY 
    currency;