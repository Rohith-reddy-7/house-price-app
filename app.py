import streamlit as st
import pickle
import pandas as pd

# Load model
try:
    with open("final_model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.title("🏠 House Price Prediction App")
st.write("Enter the house details below to predict the price.")

# User Inputs
lot_frontage = st.number_input("Lot Frontage", min_value=0.0, value=60.0)
lot_area = st.number_input("Lot Area (sq ft)", min_value=500.0, value=8000.0)
overall_quality = st.slider("Overall Quality", 1, 10, 5)
year_built = st.number_input("Year Built", min_value=1800, max_value=2026, value=2000)
gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", min_value=300.0, value=1500.0)

# Create input DataFrame
input_data = pd.DataFrame({
    "LotFrontage": [lot_frontage],
    "LotArea": [lot_area],
    "OverallQual": [overall_quality],
    "YearBuilt": [year_built],
    "GrLivArea": [gr_liv_area]
})

# Prediction
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🏡 Estimated House Price: ${prediction:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
