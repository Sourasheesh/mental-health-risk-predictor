🧠 Mental Health Risk Predictor A simple Streamlit-based web app that predicts potential mental health risk based on user inputs. The app includes user authentication (Sign Up, Login, Logout) and uses a pre-trained machine learning model to make predictions.

🚀 Features User Authentication

Sign Up with email and password

Login with existing credentials

Logout functionality

Mental Health Risk Prediction

Inputs: Age, Gender, Family history, Work interference level

Encodes inputs using pre-trained label encoders

Uses a pre-trained ML model (mental_health_model.pkl) for prediction

Interactive UI built with Streamlit

📂 Project Structure bash Copy Edit . ├── model/ │ ├── mental_health_model.pkl # Pre-trained ML model │ ├── label_encoders.pkl # Label encoders for categorical variables ├── app.py # Main Streamlit application ├── requirements.txt # Python dependencies └── README.md # Project documentation

🛠 Installation 1️⃣ Clone the repository bash Copy Edit git clone https://github.com/your-username/mental-health-risk-predictor.git cd mental-health-risk-predictor 2️⃣ Install dependencies bash Copy Edit pip install -r requirements.txt (If requirements.txt is missing, you can install manually:)

bash Copy Edit pip install streamlit pandas joblib 3️⃣ Add model files Ensure mental_health_model.pkl and label_encoders.pkl are placed in the model/ folder.

▶️ Running the App bash Copy Edit streamlit run app.py Once running, open the local URL provided by Streamlit (e.g., http://localhost:8501) in your browser.

📊 How It Works Authentication – Users must sign up or log in to access the predictor.

Input Data – Users fill in basic details:

Age

Gender

Family history of mental illness

Work interference level

Encoding & Prediction –

Inputs are encoded using saved label_encoders.pkl

The pre-trained model predicts mental health risk

Output – Displays whether the user might be at risk or not.

📜 Requirements Python 3.8+

Streamlit

Pandas

Joblib
