# Heart Disease Prediction Application

🔗 **Live Project**: [Heart Disease Predictor](https://user:1f025c1a727327ee0aff905076f3292b@heart-disease-app-tunnel-0hhbqcro.devinapps.com)

## Application Preview
![Heart Disease Prediction App](/static/images/app_preview.png)

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
