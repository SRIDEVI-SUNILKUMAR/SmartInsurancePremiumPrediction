# 🚗 Smart Insurance Premium Predictor

A Streamlit web app that predicts **insurance premium amounts** based on user-provided information like age, income, vehicle details, health score, and more.

Built using:
- 🧠 LightGBM (regressor)
- 🛠️ Scikit-learn Pipeline
- 🎨 Streamlit UI

---

## 📌 Features

- Interactive UI to input customer details
- Predicts insurance premium using a pre-trained machine learning model
- Real-time predictions — no retraining needed
- Easy deployment with Streamlit Cloud

---

## 🏁 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/smartinsurancepremiumpredictor.git
cd smartinsurancepremiumpredictor
2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the app
bash
streamlit run insurance_app.py
🌐 Live App (if deployed)
Click here to try the live app
📂 Project Structure
graphql
Copy
Edit
smartinsurancepremiumpredictor/
│
├── insurance_app.py         # Streamlit app UI
├── trained_model.pkl        # Pre-trained LightGBM model pipeline
├── requirements.txt         # Python package dependencies
├── README.md                # Project description and instructions
└── (optional) train_model.py  # Script used to train and save the model
 Model Details
Model: LightGBM Regressor (LGBMRegressor)

Preprocessing: Scikit-learn Pipeline

Numerical: Imputation + StandardScaler

Categorical: Imputation + OneHotEncoder
 Author
Sridevi Sunilkumar
