import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load your trained model
with open('final_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction App")

# Show expected features (for debugging)
st.write("Expected features:", model.feature_names_)

# Input fields for features — adjust to match your model’s training columns
st.header("Enter House Details")

# Example inputs (you can add/remove based on model.feature_names_)
lot_frontage = st.number_input("Lot Frontage", min_value=0.0, value=60.0)
lot_area = st.number_input("Lot Area (sq ft)", min_value=500.0, value=8000.0)
overall_quality = st.number_input("Overall Quality (1–10)", min_value=1, max_value=10, value=5)
year_built = st.number_input("Year Built", min_value=1800, max_value=2026, value=2000)
gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", min_value=300.0, value=1500.0)

# Create DataFrame with correct column names
input_data = pd.DataFrame({
    'LotFrontage': [lot_frontage],
    'LotArea': [lot_area],
    'OverallQual': [overall_quality],
    'YearBuilt': [year_built],
    'GrLivArea': [gr_liv_area]
})

# Reorder columns to match model training order
input_data = input_data.reindex(columns=model.feature_names_)

# Predict button
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)
        # If your model was trained on log prices, use np.exp() to revert
        st.success(f"Estimated House Price: ${np.exp(prediction[0]):,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
