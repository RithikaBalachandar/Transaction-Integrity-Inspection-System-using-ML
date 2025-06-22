import sqlite3
from flask import Flask, request, render_template
import joblib
import numpy as np
import datetime

app = Flask(__name__, template_folder="templates")

# Database setup
conn = sqlite3.connect('fraud.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS fraud_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id TEXT UNIQUE NOT NULL,
    receiver_id TEXT NOT NULL,
    amount REAL,
    transaction_date TEXT,
    flagged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

# Load models
svm_model = joblib.load('svm_model.pkl')
rf_model = joblib.load('fraud_detection_model.pkl')

# DB helpers
def add_fraud_transaction(transaction_id, receiver_id, amount=None, transaction_date=None):
    try:
        cursor.execute('''
        INSERT INTO fraud_transactions (transaction_id, receiver_id, amount, transaction_date)
        VALUES (?, ?, ?, ?)
        ''', (transaction_id, receiver_id, amount, transaction_date))
        conn.commit()
    except sqlite3.IntegrityError:
        pass

def is_receiver_fraudulent(receiver_id):
    cursor.execute('SELECT 1 FROM fraud_transactions WHERE receiver_id = ?', (receiver_id,))
    return cursor.fetchone() is not None


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input
        transaction_id = request.form.get('transaction_id')
        type_ = float(request.form['type'])
        amount = float(request.form['amount'])
        oldbalance = float(request.form['oldbalance'])
        newbalance = float(request.form['newbalance'])
        sender_id = request.form['sender_id']
        receiver_id = request.form['receiver_id']
        step = int(request.form['step'])

        reasons = []

        if is_receiver_fraudulent(receiver_id):
            reasons.append("Receiver already flagged from earlier transaction.")
            chart_data = {
                "labels": ["SVM", "Random Forest", "High Amount", "Odd Hour"],
                "values": [1, 0, 0, 0]
            }
            risk_score = 90  # High risk for known fraudulent receiver
            return render_template('result.html', pred='Fraud', receiver_id=receiver_id, reason=', '.join(reasons), risk_score=risk_score, chart_data=chart_data)

        features = np.array([[type_, amount, oldbalance, newbalance]])

        svm_pred = svm_model.predict(features)[0]
        rf_pred = rf_model.predict(features)[0]

        high_amount_flag = amount >= 0.95 * oldbalance if oldbalance > 0 else False
        odd_hour_flag = step in [1, 2, 3, 4, 5]

        if svm_pred == 1:
            reasons.append("SVM model flagged the transaction.")
        if rf_pred == 1:
            reasons.append("Random Forest model flagged the transaction.")
        if high_amount_flag:
            reasons.append("Transaction amount is suspiciously high.")
        if odd_hour_flag:
            reasons.append("Transaction occurred during odd hours.")

        chart_data = {
            "labels": ["SVM", "Random Forest", "High Amount", "Odd Hour"],
            "values": [int(svm_pred), int(rf_pred), int(high_amount_flag), int(odd_hour_flag)]
        }

        # Risk score calculation (0-100 scale)
        risk_score = (
            svm_pred * 40 +
            rf_pred * 40 +
            int(high_amount_flag) * 10 +
            int(odd_hour_flag) * 10
        )

        is_fraud = (svm_pred == 1 or rf_pred == 1 or (high_amount_flag and odd_hour_flag))

        if is_fraud:
            transaction_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            add_fraud_transaction(transaction_id, receiver_id, amount, transaction_date)
            return render_template('result.html', pred='Fraud', receiver_id=receiver_id, reason=', '.join(reasons), risk_score=risk_score, chart_data=chart_data)
        else:
            return render_template('result.html', pred='Not Fraud', risk_score=risk_score, chart_data=chart_data)

    except Exception as e:
        return f"Error occurred: {e}"


if __name__ == '__main__':
    app.run(debug=True)
