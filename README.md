❤️ Heart Disease Prediction System

A machine learning–powered web application that predicts the likelihood of heart disease based on clinical parameters. This project uses Logistic Regression for prediction and a Streamlit web interface for user interaction.

⸻

📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early detection can significantly improve treatment outcomes. This project aims to:
	•	Predict the presence of heart disease using patient health data
	•	Provide a simple and interactive web interface for predictions
	•	Demonstrate a complete end-to-end ML pipeline (training → evaluation → deployment)

The model is trained on the UCI Heart Disease Dataset.

⸻

🧠 Machine Learning Details
	•	Algorithm: Logistic Regression
	•	Problem Type: Binary Classification
	•	Target Variable: target (1 = Heart Disease, 0 = No Heart Disease)
	•	Evaluation Metrics:
	•	Accuracy
	•	ROC-AUC Score
	•	Precision, Recall, F1-score

🔍 Features Used (13)
	•	age
	•	sex
	•	cp (chest pain type)
	•	trestbps (resting blood pressure)
	•	chol (serum cholesterol)
	•	fbs (fasting blood sugar)
	•	restecg (resting ECG)
	•	thalach (maximum heart rate achieved)
	•	exang (exercise induced angina)
	•	oldpeak (ST depression)
	•	slope (slope of ST segment)
	•	ca (number of major vessels)
	•	thal (thalassemia)

⸻

🛠️ Tech Stack
	•	Python
	•	NumPy, Pandas – Data manipulation
	•	Scikit-learn – Model training & evaluation
	•	Joblib – Model persistence
	•	Streamlit – Web application

⸻

📂 Project Structure

heart-disease-prediction/
│
├── app.py                     # Streamlit application
├── heart_disease_model.pkl    # Trained ML model
├── scaler.pkl                 # StandardScaler object
├── heart.csv                  # Dataset
├── training.py                # Model training script
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation


⸻

🚀 How to Run the Project

1️⃣ Clone the Repository

git clone https://github.com/dharmajitbaro/heart_disease_prediction.git
cd heart-disease-prediction

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Train the Model (Optional)

python training.py

4️⃣ Run the Streamlit App

streamlit run app.py

The app will open in your browser at:

http://localhost:8501


⸻

🖥️ Application Features
	•	User-friendly form for medical inputs
	•	Real-time prediction
	•	Risk probability display
	•	Clear result messages:
	•	✅ No Heart Disease
	•	⚠️ Heart Disease Detected

⸻

⚠️ Medical Disclaimer

This application is intended for educational and research purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

⸻

📊 Results
	•	Achieved strong performance on test data
	•	Balanced class prediction using class_weight='balanced'
	•	ROC-AUC used for reliable medical evaluation

⸻

🌟 Future Improvements
	•	Add SHAP/LIME for model explainability
	•	Use advanced models (Random Forest, XGBoost)
	•	Deploy on Streamlit Cloud / AWS
	•	Add user authentication
	•	Store prediction history

⸻

👤 Author

Dharmajit Baro
Aspiring Machine Learning Engineer



⭐ If you like this project, give it a star on GitHub!
