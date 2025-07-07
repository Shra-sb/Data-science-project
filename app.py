
import streamlit as st
import pandas as pd
import pickle
from recommend import get_recommendations
from translate_text import translate
import shap

# Language selector
lang_code = {
    "English": "en",
    "Hindi (हिंदी)": "hi",
    "Marathi (मराठी)": "mr"
}
st.sidebar.title("🌐 Select Language")
lang = st.sidebar.selectbox("Language", list(lang_code.keys()))
lang_id = lang_code[lang]

st.set_page_config(page_title="Smart Heart Risk Predictor", layout="centered")
st.title(translate("💓 Heart Disease Prediction + Lifestyle Advice", lang_id))

model = pickle.load(open("model/heart_model.pkl", "rb"))

with st.form("input_form"):
    age = st.slider(translate("Age", lang_id), 20, 80, 40)
    cholesterol = st.slider(translate("Cholesterol", lang_id), 100, 400, 200)
    bp = st.slider(translate("Resting BP", lang_id), 80, 200, 120)
    fasting_bs = st.selectbox(translate("Fasting Blood Sugar > 120 mg/dl", lang_id), [0, 1])
    max_hr = st.slider(translate("Max Heart Rate", lang_id), 60, 200, 100)
    exercise = st.radio(translate("Do you exercise regularly?", lang_id), 
                        [translate("Yes", lang_id), translate("No", lang_id)])
    submit = st.form_submit_button(translate("Predict", lang_id))

if submit:
    input_data = pd.DataFrame([[age, cholesterol, bp, fasting_bs, max_hr]],
        columns=["Age", "Cholesterol", "RestingBP", "FastingBS", "MaxHR"])

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1] * 100

    st.subheader(translate("🩺 Prediction Result", lang_id))
    if prediction == 1:
        st.error(translate(f"High Risk of Heart Disease ({prob:.2f}%)", lang_id))
    else:
        st.success(translate(f"Low Risk of Heart Disease ({prob:.2f}%)", lang_id))

    st.subheader(translate("📋 Lifestyle Recommendations", lang_id))
    for rec in get_recommendations(age, cholesterol, bp, exercise, lang_id):
        st.write("- " + rec)
