import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the model and scaler
model = joblib.load('regression_model_1.joblib')
scaler = joblib.load('scaled.joblib')

# Streamlit app
st.title("Boston Housing Income Predictor")

st.write("Enter the housing features to predict the expected income:")

# Input fields
crim = st.number_input("CRIM", value=0.0)
zn = st.number_input("ZN", value=0.0)
indus = st.number_input("INDUS", value=0.0)
chas = st.selectbox("CHAS (Charles River dummy variable)", [0, 1])
nox = st.number_input("NOX", value=0.0)
rm = st.number_input("RM (Average number of rooms)", value=0.0)
age = st.number_input("AGE", value=0.0)
dis = st.number_input("DIS (Distance to employment centers)", value=0.0)
rad = st.number_input("RAD (Index of accessibility)", value=0)
tax = st.number_input("TAX", value=0.0)
ptratio = st.number_input("PTRATIO", value=0.0)
b = st.number_input("B (1000(Bk - 0.63)^2)", value=0.0)
lstat = st.number_input("LSTAT (% lower status)", value=0.0)

# Prediction button
if st.button("Predict Income"):
    # Create input array
    input_data = np.array([[crim, zn, indus, chas, nox, rm, age, dis,
                            rad, tax, ptratio, b, lstat]])
    
    # Scale input
    input_scaled = scaler.transform(input_data)
    
    # Predict
    predicted_income = model.predict(input_scaled)[0]
    
    st.success(f"Predicted Income: ₹{predicted_income} (in 1000s)")

