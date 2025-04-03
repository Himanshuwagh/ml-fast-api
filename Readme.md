# 🚀 Simple ML Prediction API (FastAPI)

This project is a lightweight REST API built using **FastAPI** that serves a **pre-trained dummy machine learning model**. The API accepts a numeric input via a GET request and returns a numeric prediction as JSON. It is designed for easy local use and cloud deployment on free-tier platforms like **Render**, **Railway**, or **Fly.io**.

---

## 📦 Features

- 📤 **GET /predict** endpoint for prediction
- 🧠 Loads a pre-trained `LinearRegression` (or similar) model from a `.pkl` file
- ⚡ Built using FastAPI — high performance, minimal code
- 🌐 Cloud-deployable to any free-tier hosting provider
- 🧪 Automatic Swagger documentation at `/docs`

---

## 🧠 Model Details

- Model type: `sklearn.linear_model.LinearRegression`
- Input: Single numeric float (`x`)
- Output: Predicted float value (`y`)
- Stored in: `simple_model.pkl`

This is a dummy model trained on synthetic data for demonstration.

---

## 📁 Project Structure

    .
    ├── main.py               # fast api implementation for /predict
    ├── model.py              # pre-trained dummy model script
    ├── simple_model.pkl      # model weight pickle file        
    ├── README.md                    
    ├── requirements.txt      # requirements.txt

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- `pip` package manager

### 🧪 Local Installation

1. **Clone the repo or copy the files**:

```bash
git clone https://github.com/yourusername/take_home_api.git
cd take_home_api
