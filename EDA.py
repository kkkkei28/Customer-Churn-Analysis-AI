import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. DATA LOADING & PRE-PROCESSING
# ==========================================

# Load the dataset
df = pd.read_csv('online_retail.csv', encoding='ISO-8859-1')

# Data Cleaning
df = df.dropna(subset=['CustomerID'])        # Remove rows missing CustomerID
df = df[df['Quantity'] > 0]                 # Remove non-positive quantities
df = df[df['UnitPrice'] > 0]                # Remove non-positive unit prices
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']) # Convert to datetime
df['TotalSum'] = df['Quantity'] * df['UnitPrice']     # Calculate line total

# ==========================================
# 2. RFM & CHURN ANALYSIS
# ==========================================

# Set reference date (Last date in data + 1 day)
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

# Aggregate by Customer
customer_data = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # Recency
    'InvoiceNo': 'count',                                   # Frequency
    'TotalSum': 'sum'                                       # Monetary
})

customer_data.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalSum': 'Monetary'
}, inplace=True)

# Define Churn (90+ days of inactivity)
customer_data['Is_Churn'] = (customer_data['Recency'] > 90).astype(int)

# Identify Favorite Category per Customer
customer_category_pref = df.groupby(['CustomerID', 'Description'])['TotalSum'].sum().reset_index()
favorite_category = customer_category_pref.sort_values('TotalSum', ascending=False).drop_duplicates('CustomerID')
favorite_category = favorite_category.rename(columns={'Description': 'Top_Category'})

# Merge Churn data with Category data
analysis_final = customer_data.merge(favorite_category[['CustomerID', 'Top_Category']], on='CustomerID', how='left')

# ==========================================
# 3. ADVANCED VISUALIZATION
# ==========================================

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 7))

# Scatter plot: Recency vs Frequency
scatter = sns.scatterplot(
    data=analysis_final, 
    x='Recency', 
    y='Frequency', 
    hue='Is_Churn', 
    size='Monetary', 
    sizes=(20, 500), 
    alpha=0.6, 
    palette='coolwarm'
)

plt.title('Customer Risk Profile: Recency vs Frequency (Size = Monetary Value)', fontsize=15)
plt.axvline(90, color='red', linestyle='--', label='90-Day Churn Threshold')
plt.ylabel('Frequency (Purchase Count)')
plt.xlabel('Recency (Days Since Last Purchase)')
plt.legend(title='Churn Status (1=Churn)')
plt.show()

# ==========================================
# 4. DYNAMIC AI PROMPT GENERATION
# ==========================================

def create_dynamic_ai_prompt(row):
    if row['Is_Churn'] == 1:
        customer_id = row['CustomerID']
        category = row['Top_Category']
        spent = round(row['Monetary'], 2)
        
        # Logic: If customer is in top 10% of spenders, they are "VIP"
        is_vip = spent > analysis_final['Monetary'].quantile(0.9)
        offer = "25% 'Elite Loyalty' Discount" if is_vip else "15% 'Welcome Back' Discount"
        tier = "VIP" if is_vip else "Standard"

        prompt = f"""
[Target Customer ID: {customer_id}]
- Segment: {tier} High-Value (Total spend: £{spent})
- Risk: Inactive for {row['Recency']} days.
- Past Interest: Primarily purchased '{category}'.
- Task: Generate a personalized re-engagement email.
- Offer: Include a {offer}.
- Tone: Professional, warm, and slightly exclusive (British English).
        """
        return prompt
    return "Active Customer - No automation required."

# Generate prompts for top 3 "High-Value Churned" customers
churned_high_value = analysis_final[analysis_final['Is_Churn'] == 1].sort_values('Monetary', ascending=False).head(3)
churned_high_value['AI_Prompt'] = churned_high_value.apply(create_dynamic_ai_prompt, axis=1)

# ==========================================
# 5. BUSINESS INSIGHTS OUTPUT
# ==========================================

print("\n" + "="*50)
print("EXECUTIVE SUMMARY: CUSTOMER RETENTION")
print("="*50)

# Churn Rate
churn_rate = analysis_final['Is_Churn'].mean()
print(f"Current Churn Rate: {churn_rate:.2%}")

# Monetary Comparison
avg_monetary = analysis_final.groupby('Is_Churn')['Monetary'].mean()
print(f"Avg Spend (Active):  £{avg_monetary[0]:.2f}")
print(f"Avg Spend (Churned): £{avg_monetary[1]:.2f}")

# Category Analysis
category_churn_rate = analysis_final.groupby('Top_Category').agg({'Is_Churn': ['mean', 'count']})
top_churn_cat = category_churn_rate[category_churn_rate[('Is_Churn', 'count')] > 20].sort_values(('Is_Churn', 'mean'), ascending=False).head(1)

print(f"\nCritical Category: '{top_churn_cat.index[0]}'")
print(f"Action: High churn detected in this category. Investigate product quality or shipping speed.")

print("\n" + "="*50)
print("SAMPLE AI RE-ENGAGEMENT PROMPTS")
print("="*50)
for index, row in churned_high_value.iterrows():
    print(f"\n--- Customer {row['CustomerID']} ({'VIP' if row['Monetary'] > analysis_final['Monetary'].quantile(0.9) else 'Standard'}) ---")
    print(row['AI_Prompt'])