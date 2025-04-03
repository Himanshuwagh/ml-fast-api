# take_home_model.py
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Create synthetic data
X = np.array([[i] for i in range(0, 10)])  # 0 to 9
y = np.array([2 * i + 1 for i in range(0, 10)])  # y = 2x + 1

# Train a simple model
model = LinearRegression()
model.fit(X, y)

# Save model to file
with open("simple_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as simple_model.pkl")