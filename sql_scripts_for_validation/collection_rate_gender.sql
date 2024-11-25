WITH filtered_loans AS (
    SELECT 
        l.loan_id,
        l.borrower_id,
        l.currency,
        l.principal_amount,
        b.gender
    FROM 
        loans l
    INNER JOIN 
        borrowers b ON l.borrower_id = b.borrower_id
    WHERE 
        l.maturity_date <= '2024-07-31'
),

payments_summary AS (
    SELECT 
        currency, 
        SUM(amount) AS total_collected_amount
    FROM 
        payments
    GROUP BY 
        currency
),

loans_summary_gender AS (
    SELECT 
        currency, 
        gender,
        SUM(principal_amount) AS total_principal_amount
    FROM 
        filtered_loans
    GROUP BY 
        currency, gender
)

SELECT 
    lsg.currency, 
    lsg.gender,
    ps.total_collected_amount,
    lsg.total_principal_amount,
    (ps.total_collected_amount / NULLIF(lsg.total_principal_amount, 0)) * 100 AS collections_rate
FROM 
    payments_summary ps
INNER JOIN 
    loans_summary_gender lsg ON ps.currency = lsg.currency;