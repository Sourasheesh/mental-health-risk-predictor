import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("model/mental_health_model.pkl")
label_encoders = joblib.load("model/label_encoders.pkl")

# Simulated user database
if "users" not in st.session_state:
    st.session_state.users = {"test@example.com": "1234"}  # default user
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"  # start with login page


# ---------------- SIGNUP PAGE ----------------
def signup_page():
    st.title("🧠 Mental Health Risk Predictor")
    st.subheader("Create an Account")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if email in st.session_state.users:
            st.error("❌ Email already registered.")
        elif password != confirm_password:
            st.error("❌ Passwords do not match.")
        elif email.strip() == "" or password.strip() == "":
            st.error("❌ Please fill all fields.")
        else:
            st.session_state.users[email] = password
            st.success("✅ Account created successfully! Please login.")
            st.session_state.page = "login"


# ---------------- LOGIN PAGE ----------------
def login_page():
    st.title("🧠 Mental Health Risk Predictor")
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email in st.session_state.users and st.session_state.users[email] == password:
            st.session_state.logged_in = True
            st.session_state.page = "main"
        else:
            st.error("❌ Invalid email or password.")

    if st.button("Go to Signup"):
        st.session_state.page = "signup"


# ---------------- MAIN APP PAGE ----------------
def main_page():
    st.title("🧠 Mental Health Risk Predictor (Tech Industry)")
    st.write("Answer the following questions to check if you may be at risk.")

    age = st.number_input("Age", min_value=18, max_value=100, value=25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other", "Unknown"])
    family_history = st.selectbox("Do you have a family history of mental illness?", ["Yes", "No", "Unknown"])
    work_interfere = st.selectbox(
        "If you have a mental health issue, does it interfere with work?",
        ["Never", "Rarely", "Sometimes", "Often", "Unknown"]
    )

    input_data = pd.DataFrame([[age, gender, family_history, work_interfere]],
                              columns=["Age", "Gender", "family_history", "work_interfere"])

    for col in input_data.columns:
        if col in label_encoders:
            input_data[col] = label_encoders[col].transform(input_data[col])

    if st.button("Check Risk"):
        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.error("⚠ You might be at risk for mental health issues. Consider seeking support.")
        else:
            st.success("✅ You are likely not at immediate risk.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "login"


# ---------------- ROUTING ----------------
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "signup":
    signup_page()
elif st.session_state.logged_in and st.session_state.page == "main":
    main_page()
else:
    st.session_state.page = "login"
    login_page()
