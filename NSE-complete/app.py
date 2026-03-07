import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('stocks.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    conn = get_db_connection()
    stocks = conn.execute('SELECT * FROM stocks').fetchall()
    conn.close()
    return jsonify([dict(row) for row in stocks])

@app.route('/api/stocks/<int:stock_id>', methods=['GET'])
def get_stock(stock_id):
    conn = get_db_connection()
    stock = conn.execute('SELECT * FROM stocks WHERE id = ?', (stock_id,)).fetchone()
    conn.close()
    if stock is None:
        return jsonify({'error': 'Stock not found'}), 404
    return jsonify(dict(stock))

@app.route('/api/stocks/<int:stock_id>', methods=['PUT'])
def update_stock(stock_id):
    data = request.get_json()
    conn = get_db_connection()
    conn.execute('''
        UPDATE stocks SET sym=?, name=?, price=?, chg=?, pe=?, div=?, beta=?, sector=?, mktcap=?, momentum=?, debt=?
        WHERE id=?
    ''', (data['sym'], data['name'], data['price'], data['chg'], data['pe'], data['div'], data['beta'], data['sector'], data['mktcap'], data['momentum'], data['debt'], stock_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Stock updated successfully'})

# Load the trained model
with open('model.pkl', 'rb') as f:
    ml_model = pickle.load(f)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()

    momentum_map = {'Strong': 3, 'Moderate': 2, 'Weak': 1}
    debt_map = {'low': 1, 'medium': 2, 'high': 3}
    mktcap_map = {'Large': 3, 'Medium': 2, 'Small': 1}

    features = [[
        float(data['pe']),
        float(data['div']),
        float(data['beta']),
        float(data['chg']),
        momentum_map.get(data['momentum'], 2),
        debt_map.get(data['debt'], 2),
        mktcap_map.get(data['mktcap'], 2)
    ]]

    prediction = ml_model.predict(features)[0]
    probabilities = ml_model.predict_proba(features)[0]
    confidence = round(max(probabilities) * 100, 1)

    return jsonify({
        'prediction': prediction,
        'confidence': confidence
    })

if __name__ == '__main__':
    app.run(debug=True)