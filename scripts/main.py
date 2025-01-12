import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

# Loading data...
df = pd.read_csv('heroes_data.csv')

# Clean/Removing percentage signs from data
df['Pick Rate'] = df['Pick Rate'].str.rstrip('%').astype(float)
df['Win Rate'] = df['Win Rate'].str.rstrip('%').astype(float)

# Convert character types to numbers (one-hot encoding)
df = pd.get_dummies(df, columns=['Character Type'])

# Prepare features (X) and target (y)
X = df.drop(['Character Name', 'Win Rate'], axis=1)
y = df['Win Rate']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Training model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predicting
y_pred = model.predict(X_test_scaled)

# Check how well model performed
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Print results
print(f"\nModel Performance:")
print(f"R² Score: {r2:.3f}")
print(f"Mean Squared Error: {mse:.3f}")

# Getting feature importance
importance = dict(zip(X.columns, model.feature_importances_))
sorted_importance = sorted(importance.items(), key=lambda x: x[1], reverse=True)

# Print all feature importances
print("\nAll Feature Importances:")
for feature, importance_value in sorted_importance:
    print(f"{feature}: {importance_value:.4f}")

# Plotting/Visualizing feature importance
plt.figure(figsize=(12, 6))
plt.bar(range(len(sorted_importance)), [i[1] for i in sorted_importance])
plt.xticks(range(len(sorted_importance)), [i[0] for i in sorted_importance])
plt.title('Feature Importances')
plt.tight_layout()
plt.show()
