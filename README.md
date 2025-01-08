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

3. Set up MySQL database:
```bash
# Install MySQL if not already installed
sudo apt-get update
sudo apt-get install mysql-server
sudo systemctl start mysql

# Create database
sudo mysql -e "CREATE DATABASE IF NOT EXISTS hdp;"
```

4. Configure environment variables:
- Copy `.env.example` to `.env`
- Update the values in `.env` with your configuration

### Required Environment Variables

- `MODEL_PATH`: Path to the ML model file (default: models/modal2.pkl)
  - Purpose: Specifies the location of the trained machine learning model
  - Format: Relative or absolute path to .pkl file

- `DATABASE_URL`: MySQL database connection string
  - Purpose: Database connection configuration
  - Format: mysql://username:password@host:port/hdp
  - Example format: mysql://user:pass@localhost/hdp

- `SECRET_KEY`: Flask application secret key
  - Purpose: Used for session security and CSRF protection
  - Format: Random string of characters (recommended length: 24+ characters)

- `API_KEY`: Instamojo payment gateway API key
  - Purpose: Authentication for payment processing
  - Format: Provided by Instamojo dashboard

- `AUTH_TOKEN`: Instamojo authentication token
  - Purpose: Secondary authentication for payment processing
  - Format: Provided by Instamojo dashboard

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
