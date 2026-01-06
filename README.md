# Lending Club Loan

This project explores loan-level transactional data from **Lending Club**, a peer-to-peer lending platform in the United States.  

---

## Project Description

The goal of this project is to explore loan issuance behavior and default dynamics using real-world financial data.  
Specifically, the project:

- Analyzes **time trends** in loan issuance and default rates  
- Detects **anomalous periods** with unusually high default behavior  
- Aggregates loan performance by **loan grade** and **loan purpose**  
- Builds a **baseline predictive model** to estimate the probability of loan default  


---

## Dataset

**Lending Club Loan Data**  
Source: Kaggle  
https://www.kaggle.com/datasets/adarshsng/lending-club-loan-data-csv

The dataset contains loan-level information such as:
- Loan amount and interest rate  
- Loan issue date  
- Loan status (e.g. Fully Paid, Charged Off)  
- Borrower income, debt-to-income ratio  
- Employment length  
- Loan grade and purpose 


The dataset is not included in this repository due to its size.  
Please download the CSV file from Kaggle and place it in the `data/` directory.

---

## Methodology Overview

1. **Data Loading**  
   The raw Lending Club CSV file is loaded from the `data/` directory.

2. **Data Cleaning & Preprocessing**
   - Parse loan issue dates
   - Convert loan status into a binary default indicator
   - Parse employment length
   - Remove invalid or incomplete observations

3. **Descriptive Analysis**
   - Monthly loan issuance volume
   - Monthly default rates
   - Aggregations by loan grade and loan purpose
   - Loan amount and income-based analyses

4. **Anomaly Detection**
   - Identify months with unusually high default rates
   - Anomalies are detected using a z-score–based rule

5. **Predictive Modeling**
   - Logistic regression model
   - Predicts probability of loan default
   - Model performance evaluated using ROC-AUC

6. **Visualization**
   - Time series plots
   - Bar charts by grade and purpose
   - Heatmap of default rates (grade × purpose)
   - Anomaly-highlighted default rate plot

---

## Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/vanuhibaghdasaryan/lending-club-ds-project.git
   

2. **Navigate to the project directory**
   ```bash
   cd lending-club-ds-project
   
3. **Download the dataset**
- Download the dataset from Kaggle:  
  https://www.kaggle.com/datasets/adarshsng/lending-club-loan-data-csv
- Rename the downloaded CSV file to `loan.csv`
- Place the file inside the `data/` directory

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the analysis**
   ```bash
   python main.py
   

---

## Outputs

After running `main.py`, the following outputs are automatically generated.

### Processed Data

- **`outputs/processed/monthly.csv`**  
  Monthly loan counts, average loan amounts, default rates, and anomaly flags.

- **`outputs/processed/grade_purpose.csv`**  
  Aggregated loan counts and default rates by loan grade and loan purpose.

---

### Plots

Saved in **`outputs/plots/`**, including:

- Loan issuance over time  
- Default rate over time  
- Loan issuance vs default rate  
- Default rate by loan grade  
- Default rate by loan purpose  
- Default rate heatmap (grade × purpose)  
- Default rate with anomalies highlighted  
- Loan amount distribution by default status  
- Default rate by income quantile  

---

### Model Results

- **`outputs/reports/model_results.txt`**  
  Contains the ROC-AUC score of the logistic regression model used to predict loan default.

---

## Notes & Extensions

This project uses a **baseline modeling approach** and a simple anomaly detection method for clarity and interpretability.

Possible extensions include:
- Time-based train/test splits to better respect temporal structure
- More advanced anomaly detection techniques
- Feature engineering and categorical variable encoding
- Alternative predictive models (e.g. tree-based methods)


   
