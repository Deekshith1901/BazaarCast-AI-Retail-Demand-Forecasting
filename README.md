
# 🏪 BazaarCast

### AI-Driven Retail Demand Forecasting and Pricing Intelligence System

---

## 📌 Project Overview

**BazaarCast** is an AI-powered retail analytics prototype designed to analyze historical sales data and forecast future demand using machine learning techniques. The system helps retail stakeholders understand sales trends and make data-driven decisions related to inventory planning and pricing strategies.

This project was developed as part of **Module E: Minor in AI IIT Ropar  – Individual Open Project**.

---

## 🎯 Objectives

* Analyze historical retail sales data
* Forecast future demand using machine learning
* Visualize sales trends and AI-generated predictions
* Demonstrate the practical application of AI in retail analytics

---

## 🤖 AI Technique Used

* **Machine Learning (Supervised Learning)**
* Regression-based time-series forecasting
* The model learns historical sales patterns and generalizes to unseen future periods

The AI component is a trained regression model that predicts future retail demand based on learned temporal trends.

---

## 📂 Dataset

* **Dataset Name:** Superstore Sales Dataset
* **Source:** Public dataset (Kaggle)
* **Format:** CSV

### Key Attributes:

* Order Date
* Sales
* Product Category & Sub-Category
* Region & Segment

The dataset is preprocessed and aggregated at a monthly level to support demand forecasting.

---

## ⚙️ System Architecture

1. Data ingestion from CSV
2. Data cleaning and preprocessing
3. Monthly sales aggregation
4. Feature engineering (time index)
5. Machine learning model training
6. Demand forecasting
7. Visualization and business insights

---

## 🧪 Model Evaluation

* **Metric Used:** Mean Absolute Error (MAE)
* MAE measures the average difference between actual and AI-predicted sales values
* Visual comparison of actual vs predicted sales is provided in the app

---

## 🖥️ Working Prototype

A fully functional **Streamlit web application** is included as the working prototype.

### App Features:

* Dataset exploration and visualization
* AI model training overview
* Interactive demand forecasting
* Model evaluation metrics
* Business insights and future scope

---

## 🔗 Project Resources

- 🎥 **[Demo Video](https://drive.google.com/file/d/1s-n0N-yLBmP5E1rU6cOU2yoJ5PnaMdi6/view?usp=drive_link)**  
- 📊 **[Project Presentation (PPT)](https://docs.google.com/presentation/d/1ymIwNTZ9lhwhhsi0wXmnhhTpFjgQxIcXCQv296nEsq8/edit?usp=drive_link)**  
- 📘 **[Project Report](https://docs.google.com/document/d/1Rn0sDoJIaAyGrBAna0ZHA70YPtbLW2Tzt9Sy_gNeh6I/edit?usp=drive_link)**  
- 📂 **[Dataset – Superstore Sales CSV](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)**
- 🌐 **[Live Streamlit App – BazaarCast](https://bazaarcast-ai-retail-demand-forecasting-xma4xqetawycn55jjr3l29.streamlit.app/)**

---

## ▶️ How to Run the Prototype

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Repository Structure

```
BazaarCast/
│
├── src/ # Core project modules
│ ├── data.py # Data loading & preprocessing
│ ├── model.py # Model definition
│ └── train.py # Training & evaluation logic
│
├── notebooks/ # EDA and experiments
│ └── BazaarCast.ipynb
│
├── Sample - Superstore.csv
│
├── app.py # Streamlit working prototype
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── LICENSE # MIT License
└── .gitignore # Git ignore rules
```

---

## ⚠️ Limitations

* Does not include external factors such as promotions or holidays
* Uses a static dataset (no real-time data)
* Assumes historical trends continue into the future

The system is intended as a **decision-support tool**, not an automated decision-maker.

---

## 🚀 Future Enhancements

* Integration of advanced time-series models (ARIMA, Prophet, LSTM)
* Real-time data integration
* Category and region-level demand forecasting
* Pricing optimization module

---

## 🧠 Ethical & Responsible AI Considerations

* Uses publicly available, non-personal data
* Does not involve sensitive or individual-level predictions
* Predictions are intended to assist human decision-making

---

## 👤 Author

**Project Name:** BazaarCast
**Course:** AI Applications – Module E
**Project Type:** Individual Open Project
