# Transaction Integrity Inspection System 🔍

A machine learning–powered web application designed to detect and flag fraudulent financial transactions in real time. The system uses Support Vector Machine (SVM) and Random Forest algorithms, trained on a Kaggle dataset, and provides a user-friendly interface with risk scores, fraud alerts, and downloadable reports.

---

## 🧠 Project Overview

This system ensures the integrity of transactions by identifying potential fraud using advanced ML models. It evaluates each transaction based on features such as amount, type, balance changes, and more, and classifies it as either **Fraud** or **Legitimate**.

---

## 🚀 Features

- ⚙️ Dual ML model support: SVM and Random Forest
- 📊 Real-time prediction of fraud vs. legitimate transactions
- 🧾 Displays receiver ID, reason for detection, and confidence/risk score
- 📉 Chart.js visualization for risk score (fraud probability)
- 🌗 Tailwind CSS–based responsive UI with dark mode toggle
- 🖨️ Export results as PDF for reporting purposes
- 🔐 Backend powered by Flask for seamless model integration

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, Tailwind CSS, Chart.js, JavaScript  
- **Backend:** Python, Flask  
- **ML Libraries:** Scikit-learn, Pandas, NumPy  
- **Modeling:** Support Vector Machine (SVM), Random Forest  
- **Visualization:** Chart.js, Matplotlib  
- **Deployment-ready:** Easily hostable via Flask/Streamlit platforms

---

## 📊 Dataset

- **Source:** [Kaggle – Financial Fraud Dataset]([https://www.kaggle.com](https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset/data))  
- **Attributes Used:** Type, Amount, Balance Before/After, etc.  
- **Preprocessing:** Label encoding, normalization, handling class imbalance

---

## 🧪 How It Works

1. **User inputs** transaction details through the web form  
2. **Pre-trained model** processes the data in real-time  
3. System **predicts**: Fraud or Legitimate  
4. Displays:
   - Prediction result  
   - Receiver ID  
   - Reason for prediction  
   - Confidence score with chart  
   - Export to PDF option  

---

## 📷 Screenshot Preview
<img width="928" height="603" alt="flaaaaa mm" src="https://github.com/user-attachments/assets/b00897fd-e165-488b-a6aa-1e29a803dbf6" />

<img width="811" height="512" alt="web 1" src="https://github.com/user-attachments/assets/329b20b1-3933-4d15-8783-7cb064199a11" />

<img width="866" height="571" alt="web 2" src="https://github.com/user-attachments/assets/6cd094ab-90ab-44bd-b31c-e843deaa1631" />

---

## 📝 Paper Publication

This project is published in the **International Journal of Scientific Development and Research (IJSDR)** under the title:  
**"Transaction Integrity Inspection System using Machine Learning"** – May 2025 Edition.


---

## 👩‍💻 Author

**Rithika B**  
Fresher IT Graduate | Python Developer | AI/ML Enthusiast  
[LinkedIn](www.linkedin.com/in/rithika-balachandar) • [GitHub](https://github.com/RithikaBalachandar)

---

## 📌 Future Enhancements

- Model selection toggle on UI  
- Integration with live banking APIs for transaction simulation  
- Admin dashboard with fraud trends and analytics  
- Improved explainability using SHAP or LIME

---

## 📜 License

This project is for educational purposes only.


