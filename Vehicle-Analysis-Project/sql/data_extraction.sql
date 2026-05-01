-- Query to identify delivery performance by carrier
-- This matches the "Part 1" mentioned in your README

WITH delivery_performance AS (
    SELECT 
        carrier_id,
        carrier_name,
        region,
        shipping_date,
        delivery_date,
        planned_delivery_date,
        -- Calculate the difference between actual and planned delivery
        (delivery_date - planned_delivery_date) AS days_late
    FROM logistics_table
)

SELECT 
    carrier_name,
    region,
    COUNT(*) AS total_shipments,
    AVG(days_late) AS avg_delay_days,
    -- Flagging critical delays (more than 3 days)
    SUM(CASE WHEN days_late > 3 THEN 1 ELSE 0 END) AS critical_delays
FROM delivery_performance
GROUP BY 1, 2
ORDER BY avg_delay_days DESC;