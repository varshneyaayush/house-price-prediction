import pandas as pd
import streamlit as st
import joblib
import sklearn

st.write("scikit-learn version:", sklearn.__version__)

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

model = joblib.load("house_price_model.pkl")

st.success("✅ Model Loaded Successfully")

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "bhk": [bhk],
        "bathrooms": [bathrooms],
        "built_up_area": [area],
        "city": [city],
        "property_type": [property_type]
    })

    st.write(input_data)
    st.write(input_data.dtypes)

    prediction = model.predict(input_data)

    st.success(f"🏠 Predicted Price: ₹ {prediction[0]:.2f} Lakhs")