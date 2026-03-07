import sqlite3
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load stocks from database
conn = sqlite3.connect('stocks.db')
df = pd.read_sql_query('SELECT * FROM stocks', conn)
conn.close()

# Convert categorical columns to numbers
momentum_map = {'Strong': 3, 'Moderate': 2, 'Weak': 1}
debt_map = {'low': 1, 'medium': 2, 'high': 3}
mktcap_map = {'Large': 3, 'Medium': 2, 'Small': 1}

df['momentum_score'] = df['momentum'].map(momentum_map)
df['debt_score'] = df['debt'].map(debt_map)
df['mktcap_score'] = df['mktcap'].map(mktcap_map)

# Generate label based on stock fundamentals
def generate_label(row):
    score = 0
    if row['pe'] < 10: score += 2
    elif row['pe'] < 15: score += 1
    else: score -= 1
    if row['div'] > 5: score += 2
    elif row['div'] > 2: score += 1
    if row['beta'] < 1.0: score += 1
    elif row['beta'] > 1.5: score -= 2
    if row['momentum_score'] == 3: score += 2
    elif row['momentum_score'] == 1: score -= 2
    if row['debt_score'] == 1: score += 1
    elif row['debt_score'] == 3: score -= 2
    if score >= 4: return 'Buy'
    elif score >= 1: return 'Hold'
    else: return 'Avoid'

df['label'] = df.apply(generate_label, axis=1)

# Generate variations to expand the dataset
expanded_rows = []
np.random.seed(42)
for _, row in df.iterrows():
    for _ in range(20):
        new_row = row.copy()
        new_row['pe'] = max(1, row['pe'] + np.random.uniform(-3, 3))
        new_row['div'] = max(0, row['div'] + np.random.uniform(-1, 1))
        new_row['beta'] = max(0.1, row['beta'] + np.random.uniform(-0.3, 0.3))
        new_row['chg'] = row['chg'] + np.random.uniform(-2, 2)
        new_row['label'] = generate_label(new_row)
        expanded_rows.append(new_row)

expanded_df = pd.DataFrame(expanded_rows)

# Features and target
features = ['pe', 'div', 'beta', 'chg', 'momentum_score', 'debt_score', 'mktcap_score']
X = expanded_df[features]
y = expanded_df['label']

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained successfully!")
print(f"Training samples: {len(expanded_df)}")
print(f"Label distribution:\n{y.value_counts()}")