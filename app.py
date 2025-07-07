import streamlit as st
import pandas as pd

# Load reuse suggestion data from CSV file
data = pd.read_csv('reuse_data.csv')

# App title
st.title("♻ Leather Waste Reuse Advisor")

# Subtitle
st.subheader("Enter Your Leather Waste Details")

# Input from user
waste_type = st.selectbox("Select Waste Type:", data["Waste Type"].unique())
quantity = st.number_input("Enter Quantity (in kg):", min_value=1)

# Button to get result
if st.button("Get Reuse Suggestion"):
    result = data[data["Waste Type"] == waste_type].iloc[0]
    
    st.success("Here is your suggestion:")
    st.markdown(f"🔄 *Reuse Option*: {result['Reuse Option']}")
    st.markdown(f"🏭 *Industry*: {result['Industry']}")
    st.markdown(f"💸 *Estimated Value*: {result['Estimated Value']}")
    st.markdown(f"📦 *You Entered*: {quantity} kg of {waste_type}")
