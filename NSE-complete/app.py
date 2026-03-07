from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

stocks = [
    {"sym": "KCB", "name": "KCB Group", "price": 28.50, "chg": 1.2, "pe": 8.5, "div": 6.2, "beta": 1.1, "sector": "Banking", "mktcap": "Large", "momentum": "strong", "debt": "medium"},
    {"sym": "EQTY", "name": "Equity Group", "price": 42.00, "chg": 0.8, "pe": 9.2, "div": 4.5, "beta": 1.0, "sector": "Banking", "mktcap": "Large", "momentum": "strong", "debt": "low"},
    {"sym": "SCOM", "name": "Safaricom", "price": 18.75, "chg": -0.5, "pe": 14.3, "div": 7.1, "beta": 0.8, "sector": "Telecom", "mktcap": "Large", "momentum": "neutral", "debt": "low"},
]

@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    return jsonify(stocks)

if __name__ == '__main__':
    app.run(debug=True)