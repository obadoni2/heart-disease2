# Heart Disease Prediction Application

🔗 **Live Project**: [Heart Disease Predictor](https://heart-disease-app-tunnel-q4fr1h1a.devinapps.com/doctorlogin)

## Application Preview
![Doctor Login Interface](/app/static/images/heart1.png)
![Admin Dashboard](/app/static/images/heart2.png)

## Project Improvements and Fixes

### 1. Model Loading
- Fixed model loading by ensuring correct path to modal2.pkl
- Maintained original hardcoded paths while ensuring proper file location
- Added model version compatibility checks

### 2. Database Configuration
- Migrated from MySQL to PostgreSQL using Supabase
- Implemented secure connection handling with SSL
- Added database initialization and verification scripts

### 3. Security Enhancements
- Moved sensitive credentials to environment variables
- Created .env.example for configuration reference
- Improved password handling and authentication

### 4. Application Structure
- Organized code into app/ directory for better maintainability
- Separated frontend assets into build/ directory
- Implemented proper static file handling

### 5. Deployment Setup
- Configured gunicorn for production deployment
- Set up separate frontend and backend deployments
- Added health checks and monitoring

## About
This Flask-based web application helps predict the likelihood of heart disease using machine learning. It provides both a user-friendly interface for patients and a specialized portal for healthcare professionals.

### Features
- Heart disease prediction using Random Forest Classifier
- Separate portals for patients and doctors
- Secure authentication system
- Interactive prediction interface
- Professional medical dashboard

## Technologies Used
- Python 3.8.18
- Flask 2.0.1
- scikit-learn 1.2.2
- MySQL Database
- HTML/CSS/JavaScript

## Setup Instructions
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables using `.env.example` as template
5. Run the application:
   ```bash
   python app.py
   ```

## Project Structure
- `/templates` - HTML templates
- `/static` - CSS, JavaScript, and images
- `/prediction` - ML model and prediction logic
- `/admin` - Admin portal functionality

## Contributors
- Original repository by [obadoni2](https://github.com/obadoni2/-Heart-diseases-flask)
- Enhanced and maintained by [raimonvibe](https://github.com/raimonvibe/heart-disease)
