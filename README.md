🏡 Boston Housing Price Prediction – ML Web App

- This project predicts house prices (MEDV) using the Boston Housing Dataset.
- The model is deployed using Streamlit, allowing users to enter feature values and get real-time predictions.

📌 Tech Stack

- Python
- Scikit-Learn
- Pandas
- NumPy
- Streamlit
- Joblib (for saving/loading model)

🔍 Project Workflow

- Loaded and explored dataset
- Split into features (X) and target (y → MEDV / income variable)
- Scaled numeric features using StandardScaler
- Trained Linear Regression / Ridge / Lasso models
- Saved the best model and scaler using Joblib
- Built Streamlit UI for prediction

🚀 How to Run the App

- pip install -r requirements.txt
- streamlit run app.py

📁 Project Structure

├─ app.py
├─ regression_model_1.joblib  
├─ scaled.joblib               
├─ BostonHousing.csv


🧮 Inputs Required in UI

Users need to enter the following features:
- crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat

🎯 Output

- The app returns:
- Predicted House Price (in $1000 USD)
