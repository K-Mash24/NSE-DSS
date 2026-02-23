# NSE Student Decision Support System (DSS)

A lightweight, browser-based Decision Support System for evaluating stocks listed on the Nairobi Stock Exchange (NSE). Built as a single self-contained HTML file — no installations, frameworks, or internet connection required beyond loading the page.

---

## Overview

This DSS helps investors make informed decisions about NSE-listed stocks by scoring each stock against a personalized investor profile. The system weighs multiple financial factors and returns a clear **Buy**, **Hold/Watch**, or **Avoid** recommendation along with a breakdown of what drove the score.

---

## Features

- 📈 **Live-style scrolling ticker** showing all tracked stocks and their price changes
- 🧩 **Interactive stock picker** with clickable cards for each listed company
- 📊 **Composite scoring engine** that evaluates stocks across 7 weighted factors
- 💡 **Personalized recommendations** based on the user's capital, risk tolerance, investment horizon, and goal
- 📉 **Animated score breakdown** with visual progress bars per scoring category
- ✅ **Factor tag analysis** showing positive, neutral, and negative signals in plain language

---

## How It Works

The user fills in four profile fields:
- **Capital (KES)** — how much they want to invest
- **Investment Horizon** — short, medium, or long term
- **Risk Tolerance** — low, moderate, or high
- **Investment Goal** — growth, income, or both

They then select a stock and click **Analyze**. The system runs a scoring algorithm across 7 factors and returns a score out of 100.

| Score Range | Recommendation |
|-------------|----------------|
| 65 – 100    | ✅ Consider Buying |
| 40 – 64     | 👁 Hold / Watch |
| 0 – 39      | ⚠️ Avoid / Risky |

---

## Scoring Factors

| Factor | What It Measures |
|--------|-----------------|
| Dividend Yield | Income generation potential vs. user goal |
| P/E Ratio | Whether the stock is undervalued or overpriced |
| Beta vs Risk Profile | Volatility matched against user's risk tolerance |
| Momentum | Direction and strength of recent price trend |
| Debt Levels | Financial health and balance sheet stability |
| Capital Fit | Whether the user can meaningfully deploy their budget |
| Horizon Fit | Whether the stock suits a short or long-term strategy |

---

## Technologies Used

| Language | Role |
|----------|------|
| **HTML** | Page structure — inputs, layout, and result containers |
| **CSS** | Visual design — dark theme, animations, responsive grid |
| **JavaScript** | DSS logic — scoring engine, rendering, and interactivity |

No external libraries, no backend, no database. All stock data is hardcoded in JavaScript and all logic runs entirely in the browser.

---

## Stocks Covered

| Symbol | Company | Sector |
|--------|---------|--------|
| KCB | KCB Group | Banking |
| SCOM | Safaricom | Telecom |
| EABL | East African Breweries | Consumer |
| BAT | BAT Kenya | Consumer |
| NMG | Nation Media Group | Media |
| COOP | Co-operative Bank | Banking |
| KPLC | Kenya Power | Utilities |

---

## Limitations

- Stock data is static and hardcoded — it does not pull live prices from the NSE
- Scoring weights are manually defined and not derived from a trained model
- Intended for educational purposes and should not be used as sole financial advice

---

## Author

Built as a student project to demonstrate the practical application of a Decision Support System in a real-world financial context.