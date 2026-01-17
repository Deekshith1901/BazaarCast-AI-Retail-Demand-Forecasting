import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="BazaarCast – AI Retail Forecasting",
    layout="wide"
)

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("BazaarCast 🏪")
st.sidebar.markdown("AI-Driven Retail Demand Forecasting")

section = st.sidebar.radio(
    "Navigate",
    [
        "Overview",
        "Dataset Exploration",
        "AI Model & Training",
        "Demand Forecasting",
        "Model Evaluation",
        "Business Insights"
    ]
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Sample - Superstore.csv", encoding="latin-1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df = df.sort_values("Order Date")
    return df

df = load_data()

# --------------------------------------------------
# Preprocessing: Monthly Aggregation
# --------------------------------------------------
monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)
monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)
monthly_sales["t"] = range(len(monthly_sales))

# --------------------------------------------------
# GLOBAL AI MODEL TRAINING (IMPORTANT)
# --------------------------------------------------
TEST_MONTHS = 6

train_data = monthly_sales[:-TEST_MONTHS]
test_data = monthly_sales[-TEST_MONTHS:]

model = LinearRegression()
model.fit(train_data[["t"]], train_data["Sales"])

# --------------------------------------------------
# Overview
# --------------------------------------------------
if section == "Overview":
    st.title("BazaarCast")
    st.subheader("AI-Driven Retail Demand Forecasting & Pricing Intelligence")

    st.markdown("""
    **BazaarCast** is an AI-powered retail analytics prototype that applies
    machine learning to historical sales data to forecast future demand.

    ### 🤖 Where is the AI?
    - A **machine learning regression model** is trained on historical sales
    - The model **learns temporal demand patterns**
    - It **generalizes to unseen future periods**
    - This application allows users to interact with the trained AI model
    """)

    st.markdown("### System Capabilities")
    st.markdown("""
    - Retail sales trend analysis  
    - AI-based demand forecasting  
    - Model evaluation & validation  
    - Decision-support insights for retail planning  
    """)

# --------------------------------------------------
# Dataset Exploration
# --------------------------------------------------
elif section == "Dataset Exploration":
    st.title("Dataset Exploration")

    st.markdown("### Dataset Preview")
    st.dataframe(df.head())

    start_date = df["Order Date"].min().strftime("%d %b %Y")
    end_date = df["Order Date"].max().strftime("%d %b %Y")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", df.shape[0])
    col2.metric("Total Features", df.shape[1])

    col3.markdown("### 📅 Date Range")
    col3.markdown(f"**{start_date} → {end_date}**")

    st.markdown("### Monthly Sales Trend")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(monthly_sales["Sales"])
    ax.set_title("Historical Monthly Sales")
    ax.set_ylabel("Sales")
    st.pyplot(fig)

# --------------------------------------------------
# AI Model & Training
# --------------------------------------------------
elif section == "AI Model & Training":
    st.title("AI Model & Training")

    st.markdown("""
    ### 🤖 AI Technique Used
    - **Machine Learning (Supervised Learning)**
    - Regression-based time-series forecasting
    - Learns patterns from historical retail data
    """)

    st.markdown("### Training Configuration")

    split_df = pd.DataFrame({
        "Dataset": ["Training Data", "Test Data"],
        "Number of Months": [len(train_data), len(test_data)]
    })

    st.table(split_df)

    st.markdown("### 📈 Data Used for AI Training")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(train_data["Sales"], label="Training Data")
    ax.plot(
        range(len(train_data), len(monthly_sales)),
        test_data["Sales"],
        label="Test Data",
        linestyle="--"
    )
    ax.set_title("Training vs Test Data for AI Model")
    ax.set_ylabel("Sales")
    ax.legend()
    st.pyplot(fig)

    st.success("AI model trained successfully on historical sales data.")

# --------------------------------------------------
# Demand Forecasting
# --------------------------------------------------
elif section == "Demand Forecasting":
    st.title("AI Demand Forecasting")

    future_months = st.slider(
        "Select number of future months to forecast",
        min_value=1,
        max_value=12,
        value=6
    )

    future_t = range(len(monthly_sales), len(monthly_sales) + future_months)
    future_pred = model.predict(pd.DataFrame({"t": future_t}))

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly_sales["Sales"], label="Historical Sales")
    ax.plot(
        range(len(monthly_sales), len(monthly_sales) + future_months),
        future_pred,
        label="AI Forecast",
        linewidth=3
    )
    ax.set_title("AI-Based Retail Demand Forecast")
    ax.set_ylabel("Sales")
    ax.legend()
    st.pyplot(fig)

    forecast_df = pd.DataFrame({
        "Future_Month_Index": list(future_t),
        "AI_Predicted_Sales": future_pred
    })

    st.markdown("### Forecast Output (AI Predictions)")
    st.dataframe(forecast_df)

# --------------------------------------------------
# Model Evaluation
# --------------------------------------------------
elif section == "Model Evaluation":
    st.title("Model Evaluation")

    eval_df = test_data.copy()
    eval_df["AI_Predicted_Sales"] = model.predict(eval_df[["t"]])

    mae = mean_absolute_error(
        eval_df["Sales"],
        eval_df["AI_Predicted_Sales"]
    )

    st.metric("Mean Absolute Error (MAE)", f"{mae:.2f}")

    st.markdown("""
    **Interpretation:**  
    MAE represents the average difference between actual and AI-predicted sales.
    Lower values indicate better forecasting performance.
    """)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(eval_df["Sales"].values, label="Actual Sales")
    ax.plot(eval_df["AI_Predicted_Sales"].values, label="AI Prediction")
    ax.set_title("AI Prediction vs Actual Sales")
    ax.legend()
    st.pyplot(fig)

# --------------------------------------------------
# Business Insights
# --------------------------------------------------
elif section == "Business Insights":
    st.title("Business Insights & Decision Support")

    st.markdown("""
    ### 📈 Key Insights
    - AI effectively captures long-term retail sales trends
    - Forecasts support inventory and pricing decisions
    - Helps anticipate future demand levels
    """)

    st.markdown("""
    ### ⚠️ Limitations
    - External factors (promotions, holidays) not included
    - Assumes historical trends continue
    - Designed as a **decision-support system**, not automation
    """)

    st.markdown("""
    ### 🚀 Future Enhancements
    - Advanced time-series models (ARIMA, Prophet, LSTM)
    - Real-time data integration
    - Category and region-level forecasting
    - Pricing optimization module
    """)

    st.success("BazaarCast demonstrates applied AI for retail forecasting.")
