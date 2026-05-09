import streamlit as st
import pickle
import pandas as pd

# Load pipeline
model = pickle.load(open('loan_pipeline.pkl', 'rb'))

st.set_page_config(page_title="Loan Approval Predictor 💰", layout="centered")

st.title("💰 Loan Approval Prediction")
st.write("Fill the details to check loan approval status")

# Inputs
age = st.number_input("Age", 18, 100)
gender = st.selectbox("Gender", ["male", "female"])

education = st.selectbox("Education", [
    "high school", "bachelor", "master", "phd"
])

income = st.number_input("Annual Income", 0.0, 10000000.0)

emp_exp = st.number_input("Employment Experience (years)", 0, 50)

home = st.selectbox("Home Ownership", [
    "rent", "own", "mortgage"
])

loan_amnt = st.number_input("Loan Amount", 0.0, 10000000.0)

intent = st.selectbox("Loan Intent", [
    "education", "medical", "venture", "personal", "homeimprovement"
])

interest_rate = st.number_input("Interest Rate", 0.0, 50.0)

percent_income = st.number_input("Loan % of Income", 0.0, 1.0)

cred_hist = st.number_input("Credit History Length", 0.0, 50.0)

credit_score = st.number_input("Credit Score", 300, 900)

prev_default = st.selectbox("Previous Defaults", ["yes", "no"])

# Predict
if st.button("Predict Loan Status"):

    input_data = pd.DataFrame([{
        'person_age': age,
        'person_gender': gender,
        'person_education': education,
        'person_income': income,
        'person_emp_exp': emp_exp,
        'person_home_ownership': home,
        'loan_amnt': loan_amnt,
        'loan_intent': intent,
        'loan_int_rate': interest_rate,
        'loan_percent_income': percent_income,
        'cb_person_cred_hist_length': cred_hist,
        'credit_score': credit_score,
        'previous_loan_defaults_on_file': prev_default
    }])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("❌ Loan Rejected")
    else:
        st.success("✅ Loan Approved")