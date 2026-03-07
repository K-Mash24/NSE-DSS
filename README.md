# NSE Decision Support System — Complete Version

A full-stack web application that helps investors make data-driven decisions on stocks listed on the Nairobi Securities Exchange (NSE). This is the complete version of the NSE-DSS project, extending the simple version with a Flask REST API, a SQLite database, an admin panel, and a machine learning prediction model.

---

## Project Structure

```
NSE-complete/
├── nse.html          # Main frontend — DSS interface
├── admin.html        # Admin panel — view and edit stock data
├── app.py            # Flask backend — REST API
├── database.py       # One-time database setup script
├── train_model.py    # ML model training script
├── model.pkl         # Saved Random Forest model
├── stocks.db         # SQLite database
├── requirements.txt  # Python dependencies
└── venv/             # Python virtual environment
```

---

## Features

### Frontend (`nse.html`)
- Live scrolling stock ticker across all tracked NSE companies
- Investor profile inputs — capital (KES), investment horizon, risk tolerance, and investment goal
- Clickable stock selection cards populated dynamically from the Flask API
- Multi-factor scoring engine that evaluates each stock against the investor's profile
- Results panel showing overall score, shares affordable, capital deployed, estimated dividend, beta, and ML prediction
- Animated score breakdown bars across five scoring dimensions: valuation, dividend fit, risk match, momentum, and debt levels
- Key factors panel displaying positive, neutral, and negative signals in plain language
- Buy / Hold / Avoid recommendation with personalised advice text

### Backend (`app.py`)
Built with Flask and exposes four REST API endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/stocks` | Returns all stocks from the database |
| GET | `/api/stocks/<id>` | Returns a single stock by ID |
| PUT | `/api/stocks/<id>` | Updates a stock's fields |
| POST | `/api/predict` | Returns an ML prediction for a given stock |

### Database (`stocks.db`)
SQLite database with a single `stocks` table containing 12 NSE-listed companies. Each record stores: symbol, name, price, price change, P/E ratio, dividend yield, beta, sector, market cap, momentum, and debt level.

### Admin Panel (`admin.html`)
A browser-based interface for viewing and editing stock data without touching the database or code directly. Changes are saved via the Flask PUT endpoint and reflected immediately in the main DSS.

### Machine Learning (`train_model.py` + `model.pkl`)
A Random Forest Classifier trained on the existing stock data with generated variations, expanding the training set to 240 samples. The model takes seven input features — P/E ratio, dividend yield, beta, price change, momentum, debt level, and market cap — and outputs a Buy, Hold, or Avoid prediction with a confidence percentage. The prediction is displayed as a dedicated metric card alongside the rule-based score.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask, flask-cors |
| Database | SQLite via Python's built-in `sqlite3` |
| Machine Learning | scikit-learn (Random Forest), pandas, numpy |
| Version Control | Git, GitHub |
| Development | VS Code, Git Bash, Python virtual environment |

---

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- VS Code (recommended)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/K-Mash24/NSE-DSS.git
cd NSE-DSS/NSE-complete
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/Scripts/activate   # Git Bash on Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up the database**
```bash
python database.py
```

**5. Train the ML model**
```bash
python train_model.py
```

**6. Start the Flask server**
```bash
python app.py
```

**7. Open `nse.html` in your browser**

Make sure the Flask server is running in the background before opening the frontend.

---

## How the Scoring Works

The DSS evaluates each stock against seven factors, each weighted by the investor's profile:

| Factor | What It Measures |
|--------|-----------------|
| Dividend Fit | Income generation potential weighted against the investor's goal |
| Valuation (P/E) | Whether the stock is undervalued or overpriced relative to earnings |
| Risk vs Beta | Stock volatility matched against the investor's risk tolerance |
| Momentum | Direction and strength of the recent price trend |
| Debt Level | Financial health and balance sheet stability |
| Capital Fit | Whether the investor's budget can meaningfully acquire shares |
| Horizon Fit | Whether the stock suits a short, medium, or long-term timeframe |

The final score is clamped between 0 and 100:

| Score | Recommendation |
|-------|---------------|
| 65 – 100 | ✅ Consider Buying |
| 40 – 64 | 👁 Hold / Watch |
| 0 – 39 | ⚠️ Avoid / Risky |

The ML model runs independently and provides a second opinion based on patterns learned from the stock dataset.

---

## NSE Stocks Included

| Symbol | Company | Sector |
|--------|---------|--------|
| EQTY | Equity Group Holdings | Banking |
| KCB | Kenya Commercial Bank | Banking |
| SCOM | Safaricom PLC | Telecoms |
| EABL | East African Breweries | Manufacturing |
| KPLC | Kenya Power & Lighting Co | Energy |
| BAT | British American Tobacco | Manufacturing |
| KQ | Kenya Airways | Transport |
| JUB | Jubilee Holdings | Insurance |
| DTK | Diamond Trust Bank | Banking |
| NBV | Nairobi Business Ventures | Investment |
| SBIC | Stanbic Holdings | Banking |
| KNRE | Kenya Reinsurance | Insurance |

---

## Managing Stock Data

Stock data can be updated in two ways:

- **Admin Panel** — open `admin.html` while Flask is running, click Edit on any row, update the values, and click Save. Changes are applied immediately.
- **DB Browser for SQLite** — download from [sqlitebrowser.org](https://sqlitebrowser.org), open `stocks.db`, edit via the Browse Data tab, and click Write Changes before closing.

After editing stock data, retrain the model to keep ML predictions accurate:
```bash
python train_model.py
```

---

## Limitations

- Stock data is simulated and not sourced from a live NSE market feed
- The ML model is trained on a small generated dataset and is intended for educational demonstration only
- The application runs locally and is not deployed to a public server
- No user authentication is implemented

---

## Future Improvements

- Connect to a live NSE data API for real-time prices and historical data
- Expand the ML model with a larger real-world dataset for more reliable predictions
- Build a portfolio comparison feature for evaluating multiple stocks side by side
- Deploy to a cloud platform such as Render or Railway

---

## Disclaimer

This tool is for educational purposes only and does not constitute financial advice. Always consult a licensed investment advisor before making real investment decisions. All data shown is simulated for learning purposes.

---

## Author

Built by [K-Mash24](https://github.com/K-Mash24) as a student Decision Support System project.

> For the browser-only version with no backend or dependencies, see the [NSE-simple](../NSE-simple) folder. It is a functional prototype with limited capability mostly relying on Javascript