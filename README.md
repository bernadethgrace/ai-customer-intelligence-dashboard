# AI Customer Intelligence Dashboard

This dashboard is designed as an AI-powered analytical tool to provide deep insights into financial behavior, transaction patterns, and customer fraud risks instantly by simply entering a Client ID.

---

## Project Overview

This project is an end-to-end fraud analytics dashboard designed to help analyze customer transaction behavior and identify potential fraud risks.

The dashboard combines:
- Customer profiling
- Fraud behavior monitoring
- Spending analytics
- Transaction pattern analysis
- AI-generated customer insights

The project was developed as a technical assessment and portfolio project focused on data science, analytics engineering, and dashboard development.

Due to GitHub file size limitations, only a sample feature store is included for dashboard demonstration purposes.

---

# Dashboard Features

## Customer Profile Overview

Displays important customer-level information such as:
- Credit score
- Current age
- Yearly income
- Inflow
- Savings ratio
- Account activity

---

## Fraud Risk Analysis

Fraud-focused monitoring features including:
- Fraud ratio analysis
- Fraud risk classification
- High-risk customer identification
- Fraud transaction counts
- Suspicious behavior indicators

---

## Spending Behavior Analytics

Interactive spending analysis including:
- Monthly spending trends
- Average transaction amount
- Transaction frequency
- Spending category analysis
- Merchant behavior patterns

---

## Card & Transaction Insights

Card-related and transaction-level monitoring:
- Card brand distribution
- Credit limit analysis
- Card risk indicators
- Dark web exposure flag
- Transaction error analysis

---

## AI-Generated Insights

Integrated LLM-based explanations for:
- Customer behavior summaries
- Fraud risk interpretation
- Spending pattern explanations
- Behavioral anomaly insights

---

# Tech Stack

## Programming & Analytics
- Python
- Pandas
- NumPy
- Scikit-learn

## Dashboard & Visualization
- Streamlit
- Plotly

## AI Integration
- LangChain
- Ollama LLM

## Development Tools
- VSCode
- Git
- GitHub

---

# Project Structure

```bash
TechnicalTest-PermataBank/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── client_feature_store_v2.ipynb
│
├── docs/
│
├── assets/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Dataset Description

The dataset used in this project is publicly available on Kaggle:

[Transactions Fraud Datasets on Kaggle](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets/code?utm_source=chatgpt.com)

Due to GitHub file size limitations, the raw datasets are not included in this repository.

After downloading the dataset, place the files inside:

```bash
data/
```

Expected files:

| Dataset | Description |
|---|---|
| users_data.csv | Customer demographic information |
| transactions_data.csv | Transaction history |
| cards_data.csv | Card-related information |
| train_fraud_labels.json | Fraud labels |
| mcc_codes.json | Merchant category information |

---

# Feature Engineering

Key engineered features include:

- Fraud ratio
- Total transaction count
- Average spending amount
- Monthly transaction behavior
- Credit utilization ratio
- Savings ratio
- Merchant category diversity
- Transaction error frequency
- Operational flags

---

# Installation

## Clone Repository

```bash
git clone https://github.com/bernadethgrace/fraud-detection-dashboard.git
cd fraud-detection-dashboard
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Dashboard

```bash
streamlit run app/streamlit_app.py
```

---

# Deployment

The dashboard can be deployed using:
- Streamlit Community Cloud
- Render
- Hugging Face Spaces

Recommended platform:

https://share.streamlit.io

---

# Sample Dashboard Capabilities


- Customer fraud monitoring: Real-time risk status
- Fraud risk segmentation: Low, Medium, and High risk categories
- Financial behavior analysis: Savings and spending ratios
- Customer transaction profiling: Persona identification like "Regular Bank User"
- Fraud investigation support: Deep dive transaction patterns
- Interactive analytics exploration: Question-and-answer capability with the Banking AI Assistant   

---

# Future Improvements

Potential future enhancements:
- Real-time fraud detection: Transitioning from batch to stream processing
- User authentication system: Secure login for RM and CS roles
- Database integration: Moving from static CSVs to SQL databases
- API deployment: Serving model predictions via FastAPI
- Chat Memory: Enabling stateful conversations for the AI Assistant

---

# Author

Griselda Agustina Atmadja

---

# License

This project is intended for educational, portfolio, and technical assessment purposes.

