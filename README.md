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

The dataset contains loan-level information including loan amount, interest rate, borrower characteristics, loan status, and repayment outcomes.


The dataset is not included in this repository due to its size.  
Please download the CSV file from Kaggle and place it in the `data/` directory.

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

4. **Navigate to the project directory**
   ```bash
   pip install -r requirements.txt

4. **Run the analysis**
   ```bash
   python main.py

   
