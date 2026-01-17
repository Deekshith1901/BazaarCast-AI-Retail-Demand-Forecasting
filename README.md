🏪 BazaarCast

AI-Driven Retail Demand Forecasting and Pricing Intelligence System

📌 Project Overview

BazaarCast is an AI-powered retail analytics system that forecasts future demand using historical sales data.
The project applies supervised machine learning techniques to identify demand trends and support data-driven retail decision-making.

This project was developed as part of AI Applications – Module E (Individual Open Project).

🎯 Objectives

Forecast retail demand using machine learning

Analyze historical sales trends

Build a working AI prototype

Present interpretable insights for retail planning

🤖 AI Technique Used

Supervised Machine Learning

Regression-based time-series forecasting

Trained on historical monthly sales data

The AI model learns temporal demand patterns and generalizes them to unseen future periods.

🧱 Project Structure
BazaarCast/
│
├── src/                    # Core project code
│   ├── data.py             # Data loading & preprocessing
│   ├── model.py            # ML model definition
│   └── train.py            # Training & evaluation logic
├── notebooks/              # Experiments & EDA
│   └── BazaarCast.ipynb
├── app.py                  # Streamlit working prototype
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
├── license 
└── .gitignore


🖥️ Working Prototype

The project includes a Streamlit web application that allows users to:

Explore the dataset

Understand AI model training

Generate future demand forecasts

Visualize predictions interactively

📽️ Demo Video

▶️ Demo Video Link:

Example:

https://drive.google.com/your-demo-video-link

📊 Presentation Slides

📄 Project Presentation (PPT):

Example:

https://drive.google.com/your-presentation-link

📘 Project Report
Example:

https://drive.google.com/your-report-link

▶️ How to Run the Project
1. Install Dependencies
pip install -r requirements.txt

2. Run the Prototype
streamlit run app.py

📈 Evaluation

Metric: Mean Absolute Error (MAE)

Evaluates difference between actual and predicted sales

Results show effective trend capture and stable forecasts

⚠️ Limitations

Static dataset (no real-time updates)

External factors like promotions not included

Designed as a decision-support system

🚀 Future Enhancements

Advanced time-series models (ARIMA, Prophet, LSTM)

Real-time data integration

Category & region-level forecasting

Pricing optimization module

👤 Author

Name: Deekshith Mamidi
Project Type: Individual Open Project
Course: AI Applications – Module E

🔐 AI Usage Disclosure

AI tools were used to assist with structuring code and documentation.
All modeling decisions, implementation, and evaluations were performed and validated by the student.
