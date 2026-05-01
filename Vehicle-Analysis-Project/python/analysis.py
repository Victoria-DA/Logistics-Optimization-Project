import pandas as pd

# 1. Loading the data (simulating the SQL output)
data = {
    'carrier_name': ['Carrier A', 'Carrier B', 'Carrier A', 'Carrier C'],
    'region': ['North', 'South', 'North', 'East'],
    'days_late': [2, 5, 1, 0],
    'shipping_cost': [150.00, 200.50, 145.00, 310.00]
}

df = pd.DataFrame(data)

# 2. Data Cleaning
# Ensuring all carrier names are standardized
df['carrier_name'] = df['carrier_name'].str.upper()

# 3. Simple Logic: Identify high-cost delays
# If shipping cost > 200 and it's late, mark as "Urgent Review"
df['status'] = df.apply(
    lambda x: 'Urgent Review' if (x['shipping_cost'] > 200 and x['days_late'] > 0) else 'Normal',
    axis=1
)

# 4. Final Result
print("Analysis Completed! Below is the priority list:")
print(df)

# Saving the processed report
# df.to_csv('final_logistics_report.csv', index=False)