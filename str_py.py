import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('loan_status_predict')

# Function to make prediction
def predict_loan_status(data):
    df = pd.DataFrame(data, index=[0])
    result = model.predict(df)
    return "Loan Approved" if result == 1 else "Loan Not Approved"

# Streamlit interface
st.title('Loan approval dashboard')

# Input fields
p1 = st.selectbox('Gender', [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
p2 = st.selectbox('Married', [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
p3 = st.select_slider('Dependents', [0, 1, 2, 3, 4])
p4 = st.selectbox('Education', [0, 1], format_func=lambda x: "Not Graduated" if x == 0 else "Graduated")
p5 = st.selectbox('Self Employed', [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
p6 = st.number_input('Applicant Income', min_value=0)
p7 = st.number_input('Coapplicant Income', min_value=0)
p8 = st.number_input('Loan Amount', min_value=0)
p9 = st.number_input('Loan Amount Term', min_value=0)
p10 = st.selectbox('Credit History', [0, 1])
p11 = st.selectbox('Property Area', [0, 1, 2],
                   format_func=lambda x: {0: "Rural", 1: "Semi-Urban", 2: "Urban"}.get(x))

# Predict button
if st.button('Predict Loan Status'):
    # Collect values into a dictionary
    data = {
        'Gender': p1,
        'Married': p2,
        'Dependents': p3,
        'Education': p4,
        'Self_Employed': p5,
        'ApplicantIncome': p6,
        'CoapplicantIncome': p7,
        'LoanAmount': p8,
        'Loan_Amount_Term': p9,
        'Credit_History': p10,
        'Property_Area': p11
    }

    # Prediction
    result = predict_loan_status(data)
    st.success(result)

