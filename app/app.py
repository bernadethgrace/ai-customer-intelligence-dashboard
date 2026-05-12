import streamlit as st
import pandas as pd
import json
import re
import plotly.express as px
import plotly.graph_objects as go
from langchain_ollama import OllamaLLM

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="AI Customer Intelligence",
    layout="wide"
)

st.title("🤖 AI Customer Intelligence Dashboard")

# =========================================
# LOAD LLM (OLLAMA VERSION)
# =========================================
@st.cache_resource
def load_llm():

    return OllamaLLM(
        model="phi3"
    )

llm = load_llm()

# =========================================
# SAFE HELPER
# =========================================
def safe_float(value, default=0):
    try:
        return float(value)
    except:
        return default


def safe_int(value, default=0):
    try:
        return int(float(value))
    except:
        return default


# =========================================
# LOAD DATA
# =========================================
@st.cache_data
def load_data():

    df = pd.read_csv(
        "feature_store/sample_feature_store.csv"
    )

    numeric_cols = [
        "yearly_income",
        "credit_score",
        "savings_ratio",
        "avg_monthly_inflow",
        "avg_monthly_outflow",
        "spend_income_ratio",
        "fraud_ratio",
        "travel_score",
        "digital_score",
        "night_transaction_ratio",
        "merchant_diversity_score",
        "fraud_transaction_count",
        "avg_fraud_amount",
        "days_since_last_transaction",
        "max_transactions_per_hour",
        "weekend_transaction_ratio",
        "essential_spend_ratio",
        "dining_score",
        "luxury_score",
        "current_age",
        "avg_monthly_transactions",
        "avg_active_days_per_month",
        "total_transaction_count"
    ]

    for col in numeric_cols:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            ).fillna(0)

    return df


client_feature_store = load_data()

# =========================================
# LOAD DEFINITIONS
# =========================================
@st.cache_data
def load_definitions():

    try:

        with open(
            "feature_store/definition.json",
            "r"
        ) as f:

            return pd.DataFrame(
                json.load(f)
            )

    except:

        return pd.DataFrame(
            columns=["column", "definition"]
        )


definition_df = load_definitions()

# =========================================
# IMPORTANT FEATURES
# =========================================
IMPORTANT_FEATURES = [

    # =========================
    # 💰 Financial Behavior
    # =========================
    "yearly_income",
    "total_debt",
    "credit_score",
    "spend_income_ratio",
    "savings_ratio",
    "avg_monthly_net_cashflow",

    # =========================
    # 📊 Spending Pattern
    # =========================
    "avg_monthly_inflow",
    "avg_monthly_outflow",
    "avg_monthly_transactions",
    "avg_active_days_per_month",
    "merchant_diversity_score",
    "night_transaction_ratio",
    "weekend_transaction_ratio",

    # =========================
    # 🚨 Fraud & Risk Signals
    # =========================
    "fraud_ratio",
    "fraud_transaction_count",
    "total_error_count",
    "error_ratio",
    "bad_cvv_count",
    "bad_card_number_count",
    "insufficient_balance_count",
    "technical_glitch_count",

    # =========================
    # 🧠 Behavioral Persona
    # =========================
    "travel_score",
    "digital_score",
    "dining_score",
    "luxury_score",
    "essential_spend_ratio",

    # =========================
    # 📈 Trend / Stability
    # =========================
    "spending_growth_rate",
    "income_growth_rate",
    "account_age_days",
    "customer_value_score"
]

# =========================================
# AI ENGINE
# =========================================
@st.cache_data(show_spinner=False)
def generate_ai_insight(
    client_id,
    customer_data
):

    prompt = f"""
You are an expert banking analyst.

Review the following customer data and return your analysis in JSON format.

Customer data:
{json.dumps(customer_data)}

You MUST return ONLY valid JSON with exactly this schema:

Schema:
{{
    "summary": "string",
    "personas": ["string"],
    "recommendations": ["string"]
}}

Rules:
- Output JSON only
- No markdown
- No explanation outside JSON
- Summary MUST be 200-250 words
- Provide detailed customer behavior analysis
- Include transaction habits, financial patterns, fraud signals, and actionable business insights
- Highlight unique customer characteristics
- Max 5 personas
- Max 5 recommendations
- Each recommendation under 50 characters
- Fraud risk explanation max 70 words
- NEVER repeat raw numeric metrics as labels in summary
- Always translate numerical indicators into business insight
- Focus on what the data means
- Use only provided data
- If no data, do not assume

IMPORTANT:
Ensure JSON is complete and properly closed.
Do not truncate output.
"""

    try:

        response = llm.invoke(prompt)

        if not response:
            raise Exception(
                "Empty response from Ollama"
            )

        response = str(response).strip()

        response = response.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        )

        match = re.search(
            r"\{.*\}",
            response,
            re.DOTALL
        )

        if match:
            response = match.group(0)

        parsed = json.loads(response)

        return {
            "summary": parsed.get(
                "summary",
                ""
            ),
            "personas": parsed.get(
                "personas",
                []
            ),
            "recommendations": parsed.get(
                "recommendations",
                []
            )
        }

    except Exception as e:

        return {

            "summary": f"""
Analysis unavailable.

Model encountered formatting issue while generating insight.

Fallback system activated.

Error:
{str(e)}
""",

            "personas": [
                "Digital Banking User",
                "Moderate Financial Activity"
            ],

            "recommendations": [
                "Review customer manually",
                "Monitor fraud indicators",
                "Offer digital banking products"
            ]
        }


# =========================================
# RAW TABLE BUILDER
# =========================================
@st.cache_data
def build_raw_table(
    client_row,
    definition_df
):

    df = client_row.to_frame().reset_index()

    df.columns = [
        "Feature",
        "Value"
    ]

    df = df.merge(
        definition_df,
        how="left",
        left_on="Feature",
        right_on="column"
    )

    return df[
        [
            "Feature",
            "Value",
            "definition"
        ]
    ].rename(
        columns={
            "definition": "Definition"
        }
    )


# =========================================
# SIDEBAR
# =========================================
st.sidebar.header(
    "Customer Selection"
)

client_ids = sorted(
    client_feature_store[
        "client_id"
    ].astype(str).unique()
)

selected_client = st.sidebar.selectbox(
    "Select Client ID",
    client_ids
)

st.sidebar.markdown("---")

st.sidebar.write(
    "This project is intended for educational, portfolio, and technical assessment purposes."
)

# =========================================
# GET CLIENT DATA
# =========================================
filtered = client_feature_store[
    client_feature_store[
        "client_id"
    ].astype(str) == str(selected_client)
]

if filtered.empty:

    st.error("Client not found")
    st.stop()

client_row = filtered.iloc[0]

# =========================================
# CUSTOMER DATA
# =========================================
customer_data = {}

for col in IMPORTANT_FEATURES:

    if col in client_row.index:

        customer_data[col] = safe_float(
            client_row[col]
        )

# =========================================
# SESSION STATE
# =========================================
if (
    "client" not in st.session_state
    or st.session_state.client != selected_client
):

    st.session_state.client = selected_client

    with st.spinner(
        "Generating AI insight..."
    ):

        st.session_state.ai_result = (
            generate_ai_insight(
                selected_client,
                customer_data
            )
        )

ai_result = st.session_state.ai_result

summary = ai_result.get(
    "summary",
    ""
)

personas = ai_result.get(
    "personas",
    []
)

recommendations = ai_result.get(
    "recommendations",
    []
)

# =========================================
# DASHBOARD HEADER
# =========================================
st.title(
    f"User Analytics Dashboard: {selected_client}"
)

address = client_row.get(
    "address",
    "Unknown"
)

lat = safe_float(
    client_row.get(
        "latitude",
        0
    )
)

lon = safe_float(
    client_row.get(
        "longitude",
        0
    )
)

st.caption(
    f"Address: {address} | Location: {lat}, {lon}"
)

# =========================================
# PROFILE
# =========================================
st.header(
    "📋 Customer Profile & Behavior"
)

m1, m2, m3, m4 = st.columns(4)

gender_val = str(
    client_row.get(
        "gender",
        "-"
    )
)

m1.metric(
    "Age / Gender",
    f"{safe_int(client_row.get('current_age', 0))}Y / {gender_val[:1].upper()}"
)

m2.metric(
    "Yearly Income",
    f"${safe_float(client_row.get('yearly_income', 0)):,.0f}"
)

m3.metric(
    "Credit Score",
    safe_int(
        client_row.get(
            "credit_score",
            0
        )
    )
)

m4.metric(
    "Savings Ratio",
    f"{safe_float(client_row.get('savings_ratio', 0)):.2%}"
)

# =========================================
# FINANCIAL METRICS
# =========================================
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Inflow",
    f"${safe_float(client_row.get('avg_monthly_inflow', 0)):,.2f}"
)

col2.metric(
    "Outflow",
    f"${safe_float(client_row.get('avg_monthly_outflow', 0)):,.2f}"
)

col3.metric(
    "Spend Ratio",
    f"{safe_float(client_row.get('spend_income_ratio', 0)):.2%}"
)

col4.metric(
    "Fraud Ratio",
    f"{safe_float(client_row.get('fraud_ratio', 0)):.2%}"
)

# =========================================
# CHARTS
# =========================================
col_left, col_right = st.columns(2)

with col_left:

    st.subheader(
        "Lifestyle Scoring"
    )

    categories = [
        "Travel",
        "Dining",
        "Digital",
        "Luxury"
    ]

    scores = [
        safe_float(
            client_row.get(
                "travel_score",
                0
            )
        ),

        safe_float(
            client_row.get(
                "dining_score",
                0
            )
        ),

        safe_float(
            client_row.get(
                "digital_score",
                0
            )
        ),

        safe_float(
            client_row.get(
                "luxury_score",
                0
            )
        )
    ]

    fig_radar = go.Figure()

    fig_radar.add_trace(
        go.Scatterpolar(
            r=scores,
            theta=categories,
            fill="toself"
        )
    )

    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[
                    0,
                    max(scores) + 1
                ]
            )
        ),
        showlegend=False
    )

    st.plotly_chart(
        fig_radar,
        use_container_width=True
    )

with col_right:

    st.subheader(
        "Transaction DNA"
    )

    dna_data = pd.DataFrame({

        "Metric": [
            "Weekend %",
            "Night %",
            "Merchant Diversity",
            "Essential Ratio"
        ],

        "Value": [
            safe_float(
                client_row.get(
                    "weekend_transaction_ratio",
                    0
                )
            ),

            safe_float(
                client_row.get(
                    "night_transaction_ratio",
                    0
                )
            ),

            safe_float(
                client_row.get(
                    "merchant_diversity_score",
                    0
                )
            ),

            safe_float(
                client_row.get(
                    "essential_spend_ratio",
                    0
                )
            )
        ]
    })

    fig_bar = px.bar(
        dna_data,
        x="Metric",
        y="Value",
        color="Metric",
        text_auto=".2f"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

# =========================================
# FRAUD SECTION
# =========================================
st.divider()

st.header(
    "🚨 Fraud & Risk Behavior Analysis"
)

f1, f2, f3 = st.columns(3)

fraud_ratio = safe_float(
    client_row.get(
        "fraud_ratio",
        0
    )
)

if fraud_ratio >= 0.05:
    fraud_status = "🚨 HIGH RISK"
    color = "#FF4B4B"

elif fraud_ratio >= 0.01:
    fraud_status = "⚠️ MEDIUM RISK"
    color = "#FFA500"

else:
    fraud_status = "✅ LOW RISK"
    color = "#00CC96"

f1.markdown(
    f"### Status: <span style='color:{color}'>{fraud_status}</span>",
    unsafe_allow_html=True
)

f2.metric(
    "Fraud Ratio",
    f"{fraud_ratio:.2%}"
)

f3.metric(
    "Overall Error Ratio",
    f"{safe_float(client_row.get('error_ratio', 0)):.2%}"
)

f01, f02, f03 = st.columns(3)

f01.metric(
    "Fraud Txn Count",
    f"{safe_int(client_row.get('fraud_transaction_count', 0))}"
)

f02.metric(
    "Error Txn Count",
    f"{safe_int(client_row.get('total_error_count', 0))}"
)

f03.metric(
    "Avg Fraud Amount",
    f"${safe_float(client_row.get('avg_fraud_amount', 0)):,.2f}"
)

# =========================================
# DETAIL ANALYSIS
# =========================================
col_left, col_right = st.columns([1, 1])

with col_left:

    st.subheader(
        "🔐 Authentication Failures"
    )

    auth_data = {

        "CVV":
            safe_int(
                client_row.get(
                    "bad_cvv_count"
                )
            ),

        "Card Num":
            safe_int(
                client_row.get(
                    "bad_card_number_count"
                )
            ),

        "Exp Date":
            safe_int(
                client_row.get(
                    "bad_expiration_count"
                )
            ),

        "PIN":
            safe_int(
                client_row.get(
                    "bad_pin_count"
                )
            ),

        "Zipcode":
            safe_int(
                client_row.get(
                    "bad_zipcode_count"
                )
            )
    }

    fig_auth = go.Figure(
        go.Bar(
            x=list(auth_data.values()),
            y=list(auth_data.keys()),
            orientation="h",
            marker_color="royalblue"
        )
    )

    fig_auth.update_layout(
        height=300,
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )

    st.plotly_chart(
        fig_auth,
        use_container_width=True
    )

with col_right:

    st.subheader(
        "📉 Operational & Stress Indicators"
    )

    m1, m2 = st.columns(2)

    m1.metric(
        "Insufficient Bal. Ratio",
        f"{safe_float(client_row.get('insufficient_balance_ratio', 0)):.2%}"
    )

    m2.metric(
        "Tech Glitch Ratio",
        f"{safe_float(client_row.get('technical_glitch_ratio', 0)):.2%}"
    )

    st.info(f"""
**Contextual Flags:**
- Insufficient Balance: {safe_int(client_row.get('insufficient_balance_count'))} times
- Technical Glitches: {safe_int(client_row.get('technical_glitch_count'))} occurrences
- Auth Errors: {safe_int(client_row.get('auth_error_count'))} total
""")

# =========================================
# TRANSACTION PATTERN
# =========================================
with st.expander(
    "🔍 Deep Dive Transaction Pattern"
):

    c1, c2, c3 = st.columns(3)

    c1.write(
        f"**Days Since Last Txn:** {safe_int(client_row.get('days_since_last_transaction'))} days"
    )

    c2.write(
        f"**Max Txn/Hour:** {safe_int(client_row.get('max_transactions_per_hour'))}"
    )

    c3.write(
        f"**Total Error Count:** {safe_int(client_row.get('total_error_count'))}"
    )

# =========================================
# AI RESULT
# =========================================
left, right = st.columns([2, 1])

with left:

    st.subheader("🧠 AI Summary")

    st.write(summary)

    st.subheader("👤 Personas")

    for p in personas:
        st.success(p)

with right:

    st.subheader("🎯 Recommendations")

    for r in recommendations:
        st.info(r)

# =========================================
# CHATBOT
# =========================================
st.divider()

st.subheader(
    "💬 Banking AI Assistant"
)

question = st.text_input(
    "Ask about this customer",
    placeholder="e.g. Is this customer eligible for a credit increase?"
)

if st.button("Analyze") and question:

    chat_prompt = f"""
Customer data:
{json.dumps(customer_data)}

Question:
{question}

Rules:
- Answer shortly
- Professional tone
- Give recommendation
- Do not assume missing data
"""

    with st.spinner("Thinking..."):

        try:

            response = llm.invoke(
                chat_prompt
            )

            st.write(response)

        except Exception as e:

            st.error(
                f"Ollama Error: {str(e)}"
            )

# =========================================
# RAW TABLE
# =========================================
with st.expander(
    "🔍 View Raw Features"
):

    raw_df = build_raw_table(
        client_row,
        definition_df
    )

    st.dataframe(
        raw_df,
        use_container_width=True
    )