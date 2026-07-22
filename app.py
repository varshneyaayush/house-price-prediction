import streamlit as st
import joblib

st.set_page_config(page_title="House Price Prediction")

st.title("🏠 House Price Prediction")
st.write("Welcome to the House Price Prediction App")

bhk = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=2)
area = st.number_input("Built-up Area (sq ft)", min_value=100, value=1000)

bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
city = st.selectbox(
    "Select City",
    ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Pune", "Chennai"]
)

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "Villa", "Independent House", "Studio"]
)

if st.button("Predict Price"):
    st.success("Prediction button clicked!")

model = joblib.load("house_price_model.pkl")

st.success("✅ Model Loaded Successfully")