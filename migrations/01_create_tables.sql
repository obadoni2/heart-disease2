-- Create tables for Heart Disease Prediction Flask Application

-- Users table
CREATE TABLE IF NOT EXISTS hdpuser (
    id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(120) NOT NULL,
    LastName VARCHAR(120) NOT NULL,
    Email VARCHAR(120) NOT NULL,
    Ph_no VARCHAR(20) NOT NULL,
    Profession VARCHAR(12) NOT NULL,
    Username VARCHAR(120) NOT NULL,
    password VARCHAR(120) NOT NULL
);

-- Doctors table
CREATE TABLE IF NOT EXISTS doclog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(120) NOT NULL,
    LastName VARCHAR(120) NOT NULL,
    Ph_no VARCHAR(20) NOT NULL,
    Profession VARCHAR(12) NOT NULL,
    Username VARCHAR(120) NOT NULL,
    password VARCHAR(120) NOT NULL,
    Email VARCHAR(120) NOT NULL
);

-- Admin table
CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(120) NOT NULL,
    Password VARCHAR(120) NOT NULL
);

-- Emails table
CREATE TABLE IF NOT EXISTS emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Email VARCHAR(120) NOT NULL
);

-- Dataset table
CREATE TABLE IF NOT EXISTS dataset (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Age INT NOT NULL,
    sex INT NOT NULL,
    Cp INT NOT NULL,
    Trestbps INT NOT NULL,
    Chol INT NOT NULL,
    fbs INT NOT NULL,
    Restecg INT NOT NULL,
    Thalach INT NOT NULL,
    Exang INT NOT NULL,
    Oldpeak INT NOT NULL,
    Slope INT NOT NULL,
    Thal INT NOT NULL,
    Target INT NOT NULL
);
