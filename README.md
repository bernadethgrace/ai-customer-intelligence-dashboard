# AI Customer Intelligence Dashboard

An AI-powered banking analytics dashboard designed to analyze customer financial behavior, detect fraud risks, and generate intelligent customer insights using Large Language Models (LLMs).

The dashboard allows users to explore customer profiles, transaction behavior, spending patterns, and fraud indicators simply by entering a Client ID.

---

# Live Demo

### Streamlit App
https://ai-customer-intelligence.streamlit.app/

### GitHub Repository
https://github.com/bernadethgrace/-ai-customer-intelligence-dashboard

---

## Project Overview

This project was developed as an AI-powered customer intelligence and fraud analytics solution for banking use cases.


The dashboard combines:
- Customer profiling
- Fraud risk analysis
- Spending behavior analytics
- Transaction monitoring
- AI-generated customer insights
- LLM-powered banking assistant

The project focuses on:
- Data analytics
- Feature engineering
- Fraud intelligence
- Financial behavior analysis
- AI integration in banking dashboards

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
- Transaction anomaly insights

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

## AI-Powered Banking Assistant

The dashboard includes an integrated LLM-powered assistant capable of generating:

- Customer summaries
- Fraud risk explanations
- Behavioral insights
- Spending pattern interpretations
- Customer persona analysis

---

# Cloud Deployment Migration

Initially, the application used Ollama with a local LLM setup through `app.py`.

However, Ollama-based local inference could not run properly on Streamlit Community Cloud because the deployment environment does not support running local LLM servers.

To make the dashboard deployable online, the architecture was migrated to use the Groq API for cloud-based inference.

As part of this migration:

- `app.py` was replaced with `streamlit_app.py`
- Ollama integration was removed
- Groq + Llama 3 integration was added
- The application became fully compatible with Streamlit Cloud deployment

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
- Groq API
- Llama 3

## Development Tools
- VSCode
- Git
- GitHub

---

# Project Structure

```bash
home//
│
├── .devcontainer/
│
├── app/
│   ├── streamlit_app.py
│   ├── helper_functions.py
│   └── utils.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── drafts/
│
├── feature_store/
│
├── notebooks/
│   └── client_feature_store_v2.ipynb
│
├── venv/
│
├── .gitignore
├── README.md
├── requirements.txt
├── requirements-local.txt
├── runtime.txt
└── logs.log
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
- Customer Operational flags

---

# Installation

## Clone Repository

```bash
git clone https://github.com/bernadethgrace/-ai-customer-intelligence-dashboard.git

cd -ai-customer-intelligence-dashboard
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


### For Streamlit Cloud Deployment (Groq Version)

Use this for the deployed cloud application:

```bash
pip install -r requirements.txt
```

This version uses:
- Groq API
- Cloud-based LLM inference
- `streamlit_app.py`

---

### For Local Ollama Development

Use this if you want to run the local Ollama version:

```bash
pip install -r requirements-local.txt
```

This version uses:
- Ollama local models
- Local LLM inference
- `app.py`


---

# Environment Variables

Create a `.env` file in the root directory:

```bash
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:
https://console.groq.com/keys

---

# Run the Dashboard

## Streamlit Cloud / Groq Version

Run the cloud-compatible version using:

```bash
streamlit run app/streamlit_app.py
```

This version uses:
- Groq API
- Cloud deployment setup
- Streamlit Community Cloud compatible architecture

---

## Local Ollama Version

Run the local LLM version using:

```bash
streamlit run app/app.py
```

This version uses:
- Ollama local models
- Local inference setup
- Requires Ollama installed and running locally

---

# Deployment

The dashboard is deployed using Streamlit Community Cloud.

Live App:
https://ai-customer-intelligence.streamlit.app/

The migration from Ollama to Groq was necessary to support cloud deployment and online accessibility.


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

- Real-time fraud detection pipeline
- Database integration (PostgreSQL / BigQuery)
- FastAPI model serving
- Authentication & role management
- RAG-based banking knowledge assistant
- Chat memory & conversation history
- Real-time streaming analytics

---

# Author

**Griselda Agustina Atmadja**

- Data Science & AI Enthusiast
- Banking Analytics & Fraud Intelligence Projects

---

# License

This project is intended for:

- Educational purposes
- Portfolio showcase
- Technical assessments
- AI & analytics demonstrations
```

