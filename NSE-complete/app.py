import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

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

if __name__ == '__main__':
    app.run(debug=True)