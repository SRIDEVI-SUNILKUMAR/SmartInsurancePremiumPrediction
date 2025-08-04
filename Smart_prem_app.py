#!/usr/bin/env python
# coding: utf-8

# In[ ]:
 

import streamlit as st
import pandas as pd
import joblib

# Load trained model pipeline
model_pipeline = joblib.load("C:/Users/Lenovo/Documents/Guvi/Project_3/trained_model.pkl")

# Page config
st.set_page_config(
    page_title="🚗 Insurance Premium Predictor",
    page_icon="💰",
    layout="centered"
)

# Header banner
st.markdown(
    """
    <h1 style='text-align: center; color: #4B8BBE;'>
        💡 Insurance Premium Prediction App
    </h1>
    <p style='text-align: center; font-size: 18px; color: #306998;'>
        Enter the details below to estimate your insurance premium!
    </p>
    """,
    unsafe_allow_html=True
)

# Sidebar instructions
st.sidebar.header("📝 How to use")
st.sidebar.write("""
- Fill in your details on the main page.
- Click **Predict Premium Amount**.
- Get your personalized premium estimate instantly.
""")


# User input form
def user_input_features():
    col1, col2 = st.columns(2)

    with col1:
        Age = st.number_input("Age", min_value=18, max_value=100, value=30)
        Gender = st.selectbox("Gender", ["Male", "Female"])
        Annual_Income = st.number_input("Annual Income ($)", min_value=0, value=50000, step=1000)
        Marital_Status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
        Number_of_Dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0)
        Education_Level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
        Occupation = st.selectbox("Occupation", ["Employed", "Self-Employed", "Unemployed"])
        Health_Score = st.slider("Health Score (0-100)", 0, 100, 75)

    with col2:
        Location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])
        Policy_Type = st.selectbox("Policy Type", ["Basic", "Comprehensive", "Premium"])
        Previous_Claims = st.number_input("Previous Claims", min_value=0, value=0)
        Vehicle_Age = st.number_input("Vehicle Age (years)", min_value=0, value=3)
        Credit_Score = st.number_input("Credit Score", min_value=0, max_value=1000, value=700)
        Insurance_Duration = st.number_input("Insurance Duration (years)", min_value=1, max_value=30, value=1)
        Smoking_Status = st.selectbox("Smoking Status", ["Yes", "No"])
        Exercise_Frequency = st.selectbox("Exercise Frequency", ["Daily", "Weekly", "Monthly", "Rarely"])
        Property_Type = st.selectbox("Property Type", ["House", "Apartment", "Condo"])

    # Combine into DataFrame
    data = {
        "Age": Age,
        "Annual Income": Annual_Income,
        "Number of Dependents": Number_of_Dependents,
        "Health Score": Health_Score,
        "Previous Claims": Previous_Claims,
        "Vehicle Age": Vehicle_Age,
        "Credit Score": Credit_Score,
        "Insurance Duration": Insurance_Duration,
        "Gender": Gender,
        "Marital Status": Marital_Status,
        "Education Level": Education_Level,
        "Occupation": Occupation,
        "Location": Location,
        "Policy Type": Policy_Type,
        "Smoking Status": Smoking_Status,
        "Exercise Frequency": Exercise_Frequency,
        "Property Type": Property_Type
    }

    features = pd.DataFrame(data, index=[0])
    return features


# Get input
input_df = user_input_features()

# Prediction button
if st.button("💸 Predict Premium Amount", use_container_width=True):
    with st.spinner("Calculating premium..."):
        try:
            prediction = model_pipeline.predict(input_df)[0]
            st.success(
                f"💰 **Estimated Insurance Premium:**  \n"
                f"### ${prediction:,.2f}"
            )
        except Exception as e:
            st.error(f"❌ Prediction failed: {e}")



