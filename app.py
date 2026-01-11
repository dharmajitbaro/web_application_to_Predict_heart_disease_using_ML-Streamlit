import streamlit as st
import numpy as np
import joblib

# Load model & scaler
model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

st.title("❤️ Heart Disease Prediction App")
st.write("Predict 10-year risk of heart disease using patient health data")

# Input fields
male = st.selectbox("Gender", ("Female", "Male"))
age = st.number_input("Age", 20, 100, 45)
education = st.selectbox("Education Level", [1, 2, 3, 4])
currentSmoker = st.selectbox("Current Smoker", ("No", "Yes"))
cigsPerDay = st.number_input("Cigarettes Per Day", 0, 100, 0)
BPMeds = st.selectbox("On BP Medication", ("No", "Yes"))
prevalentStroke = st.selectbox("History of Stroke", ("No", "Yes"))
prevalentHyp = st.selectbox("Hypertension", ("No", "Yes"))
diabetes = st.selectbox("Diabetes", ("No", "Yes"))
totChol = st.number_input("Total Cholesterol (mg/dL)", 100, 600, 200)
sysBP = st.number_input("Systolic BP", 80, 250, 120)
diaBP = st.number_input("Diastolic BP", 50, 150, 80)
BMI = st.number_input("BMI", 10.0, 60.0, 25.0)
heartRate = st.number_input("Heart Rate", 40, 200, 75)
glucose = st.number_input("Glucose Level", 40, 400, 80)

# Convert inputs to numeric
input_data = np.array([[ 
    1 if male == "Male" else 0,
    age,
    education,
    1 if currentSmoker == "Yes" else 0,
    cigsPerDay,
    1 if BPMeds == "Yes" else 0,
    1 if prevalentStroke == "Yes" else 0,
    1 if prevalentHyp == "Yes" else 0,
    1 if diabetes == "Yes" else 0,
    totChol,
    sysBP,
    diaBP,
    BMI,
    heartRate,
    glucose
]])

# Predict button
if st.button("Predict Heart Disease Risk"):
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Disease\n\nProbability: {probability:.2%}")
    else:
        st.success(f"✅ Low Risk of Heart Disease\n\nProbability: {probability:.2%}")