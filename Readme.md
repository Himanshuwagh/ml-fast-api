## 🚀 Simple ML Prediction API (FastAPI)

This project is a lightweight REST API built using **FastAPI** that serves a **pre-trained dummy machine learning model**. The API accepts a numeric input via a GET request and returns a numeric prediction as JSON. It is designed for easy local use and cloud deployment on free-tier platforms like **Render**

---

### 📦 Features

- 📤 **GET /predict** endpoint for prediction
- 🧠 Loads a pre-trained `LinearRegression` model from a `.pkl` file
- ⚡ Built using FastAPI — high performance, minimal code
- 🧪 Automatic Swagger documentation at `/docs`

---

### 🧠 Model Details

- Model type: `sklearn.linear_model.LinearRegression`
- Input: Single numeric float (`x`)
- Output: Predicted float value (`y`)
- Stored in: `simple_model.pkl`

This is a dummy model trained on synthetic data for demonstration.

---

### 📁 Project Structure

    .
    ├── main.py               # fast api implementation for /predict
    ├── model.py              # pre-trained dummy model script
    ├── simple_model.pkl      # model weight pickle file        
    ├── README.md                    
    ├── requirements.txt      # requirements.txt

---

### ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- `pip` package manager

#### 🧪 Local Installation

Clone the repo:

```bash
git clone https://github.com/Himanshuwagh/ml-fast-api.git
cd ml-fast-api
```
Install the libraries
```
pip install -r requirements.txt
```
Run locally using FastAPI
```
uvicorn main:app --reload
```

### 🚨 Link to the deployed on cloud : https://ml-fast-api.onrender.com

### 📡 API Usage

#### `GET /predict`

This endpoint returns a numeric prediction based on a single numeric input.

#### 🔹 How to Call

You must pass the input `x` as a **query parameter** in the URL.

#### 📘 Example:
```
GET https://ml-fast-api.onrender.com/predict?x=7.0
```
> 👆 This means you're sending the value `5.3` as input to the model via the `x` parameter.

#### ✅ Response:

```json
{
  "prediction": 15.0
}
```

#### Assumptions
- Input is a clean float value (no NaNs, invalids)

- Model accepts a single feature as input

#### Possible Improvements (with more time)

- Add input validation/range checks

- Serve multiple models or versions via route params

- Add Docker support for containerized deployments

- Add logging, metrics, and request tracing

- Implement and user Friendly UI
