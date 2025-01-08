# Heart Disease Prediction Flask Application

A Flask web application for heart disease prediction using machine learning.

## Environment Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
- Copy `.env.example` to `.env`
- Update the values in `.env` with your configuration

### Required Environment Variables

- `MODEL_PATH`: Path to the ML model file (default: models/modal2.pkl)
- `SQLALCHEMY_DATABASE_URI`: MySQL database connection string
- `API_KEY`: Instamojo API key
- `AUTH_TOKEN`: Instamojo authentication token

## Features

- User Registration and Authentication
- Heart Disease Prediction
- Payment Integration
- Admin Dashboard
- Doctor Management

## Running the Application

```bash
python app.py
```

The application will be available at http://localhost:5000
