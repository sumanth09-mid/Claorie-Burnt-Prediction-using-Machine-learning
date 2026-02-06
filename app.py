import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('model/calorie_gbr_model.pkl')

# Streamlit UI Config
st.set_page_config(page_title="🔥 Calories Burnt Predictor", layout="centered")

# App Title
st.title("🔥 Calories Burn Prediction App")
st.write("Enter your details below and the app will predict calories burnt during exercise.")

# Sidebar Inputs
st.sidebar.header("User Inputs")

gender = st.sidebar.selectbox("Gender", ("Male", "Female"))
gender = 0 if gender == "Male" else 1

age = st.sidebar.number_input("Age (years)", min_value=10, max_value=80, value=25)

height_cm = st.sidebar.number_input("Height (cm)", min_value=100, max_value=220, value=170)
weight_kg = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)

# Calculate BMI
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
st.sidebar.write(f"**Calculated BMI:** {bmi:.2f}")

duration = st.sidebar.number_input("Duration (mins)", min_value=1, max_value=300, value=60)
heart_rate = st.sidebar.number_input("Heart Rate (bpm)", min_value=40, max_value=220, value=120)
body_temp = st.sidebar.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.5)

# Additional engineered features
workout_intensity = duration * (heart_rate / 100)
temp_rise_per_min = (body_temp - 36.5) / duration
st.sidebar.write(f"**Calculated Workout_Intensity:** {workout_intensity:.2f}")
st.sidebar.write(f"**Calculated Temp_rise_per_min:** {temp_rise_per_min:.2f}")

# Prepare input for model
input_data = np.array([[gender, age, height_cm, weight_kg, duration,
                        heart_rate, body_temp, bmi, workout_intensity, temp_rise_per_min]])

if st.sidebar.button("Predict Calories Burnt"):
    prediction = model.predict(input_data)[0]

    st.success(f"🔥 **Estimated Calories Burnt:** {prediction:.2f} kcal")

    st.subheader("📊 BMI Category")
    if bmi < 18.5:
        st.info("Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal weight ✅")
    elif 25 <= bmi < 29.9:
        st.warning("Overweight ⚠️")
    else:
        st.error("Obese ❗")

st.markdown("---")
st.write("📎 *Model uses Age, Gender, BMI, Duration, Heart Rate, Body Temp & engineered workout features.*")
