# Customer Churn Analysis & AI-Driven Re-engagement Strategy

## 📌 Project Overview
This project addresses a critical business challenge in e-commerce: **Customer Retention**. Using the **Online Retail Dataset**, I developed a Python-based analytics pipeline that segments customers using **RFM (Recency, Frequency, Monetary)** modeling and automates personalized marketing strategies using **LLM (Large Language Model) Prompt Engineering**.

### 🎯 Key Objectives
* Identify high-value customers at risk of churning (90+ days of inactivity).
* Analyze geographic and category-specific churn patterns.
* Automate the generation of hyper-personalized re-engagement emails to improve LTV (Lifetime Value).

---

## 🛠️ Tech Stack & Methodology
* **Language:** Python 3.x
* **Libraries:** Pandas (Data Wrangling), Matplotlib/Seaborn (Visualization), NumPy
* **Framework:** RFM Segmentation
* **AI Integration:** LLM Prompt Orchestration for personalized CRM

---

## 📊 Analysis Workflow

### 1. Data Cleaning & Pre-processing
Ensured data integrity by handling missing Customer IDs and filtering out transactional anomalies (negative quantities/prices) to focus on revenue-generating behavior.

### 2. RFM Modeling
Calculated three core metrics for each customer:
* **Recency:** Days since the last purchase.
* **Frequency:** Total number of transactions.
* **Monetary:** Total revenue generated.

### 3. Churn Definition
Customers with **Recency > 90 days** are flagged as `Is_Churn`. This segment is further analyzed to prioritize "High-Value Churn" (top 10% spenders) for immediate recovery.

---

## 📈 Key Insights
* **Churn Rate:** [Insert your calculated churn rate, e.g., 25.4%]
* **Monetary Gap:** Active customers spend an average of **£[X]**, while churned customers represent an average loss of **£[Y]** per head.
* **Critical Categories:** Identified specific product categories (e.g., [Insert Category Name]) with disproportionately high churn rates, signaling potential quality or supply chain issues.

---

## 🤖 AI-Powered Personalized Marketing
Instead of generic "We miss you" emails, this pipeline generates **dynamic prompts** based on:
1. **Customer Tier:** (VIP vs. Standard)
2. **Product Preference:** (Top purchased category)
3. **Monetary Value:** (Adjusted discount offers)

**Example Generated Prompt:**
> "[Target Customer ID: 12345] - Segment: VIP High-Value. Risk: Inactive for 110 days. Past Interest: 'Regency Teapot'. Task: Generate a warm, exclusive re-engagement email with a 25% 'Elite Loyalty' discount."

---

## 🚀 Strategic Recommendations
1. **Prioritize "Whales":** Allocate 70% of the retention budget to the top 20% of churned customers by Monetary value.
2. **Category Deep-Dive:** Investigate the "Critical Categories" identified in the analysis to resolve underlying churn drivers.
3. **CRM Automation:** Integrate the dynamic prompt logic into automated email workflows to scale personalized outreach.

---

## 📁 Repository Structure
* `online_retail.csv`: Transactional dataset (Note: Large files may require external links).
* `churn_analysis.py`: Main analysis script.
* `visualizations/`: Exported charts and graphs.
* `README.md`: Project documentation.

---

## 👤 Author
* **Name:** Kei Ishikawa
* **Location:** Toronto, Canada
* **Desired Role:** Marketing Analyst / Business Analyst / Data Analyst
* **LinkedIn:** [https://www.linkedin.com/in/kei-ishikawa-9798b9345/]
