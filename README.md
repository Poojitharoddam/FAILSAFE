# FAILSAFE – AI-Powered Student Failure Risk Prediction System

## Overview

FAILSAFE is an Explainable Artificial Intelligence (XAI) based web application designed to identify students who are at risk of academic failure at an early stage. The system analyzes academic, behavioral, and demographic factors and predicts the likelihood of student failure, enabling educators to provide timely interventions and support.

The project combines Machine Learning, Explainable AI, and Web Technologies to create a practical decision-support system for educational institutions.

---

## Problem Statement

Educational institutions often struggle to identify students who are likely to fail before their academic performance significantly declines.

Traditional monitoring methods are reactive and depend heavily on manual observation.

FAILSAFE addresses this challenge by:

* Predicting students at risk of failure.
* Explaining the reasons behind predictions.
* Recommending suitable intervention strategies.
* Supporting data-driven academic decision making.

---

## Objectives

* Predict student academic risk using Machine Learning.
* Provide explainable predictions using SHAP.
* Assist faculty in early intervention planning.
* Improve student success and retention rates.
* Develop a full-stack web application for educational analytics.

---

## Features

### Student Risk Prediction

Predicts whether a student is at risk of academic failure.

### Explainable AI

Uses SHAP (SHapley Additive exPlanations) to explain model predictions.

### Risk Probability

Displays the probability of student failure.

### Intervention Recommendations

Suggests corrective actions based on predicted risk.

### Interactive Dashboard

User-friendly interface built using React.js.

### Secure Backend

FastAPI backend with JWT Authentication support.

### Database Support

PostgreSQL integration for storing student records and predictions.

---

## Technology Stack

### Frontend

* React.js
* HTML5
* CSS3
* Axios

### Backend

* FastAPI
* Python

### Database

* PostgreSQL

### Machine Learning

* XGBoost Classifier
* Scikit-Learn
* Pandas
* NumPy

### Explainable AI

* SHAP

### Authentication

* JWT Authentication

### Version Control

* Git
* GitHub

---

## Dataset

### Dataset Used

UCI Student Performance Dataset

### Source

Kaggle / UCI Machine Learning Repository

### Dataset Characteristics

* Student demographic information
* Family background
* Academic history
* Attendance records
* Study habits
* Extra-curricular activities

---

## Input Features Used

The prediction system uses the following inputs:

* Age
* Mother's Education (Medu)
* Father's Education (Fedu)
* Travel Time
* Study Time
* Previous Failures
* Internet Access
* Health Status
* Absences
* Extra Activities Participation

---

## Machine Learning Model

### Algorithm

XGBoost Classifier

### Target Variable

Student is classified as:

* At Risk (1) → Final Grade < 10
* Safe (0) → Final Grade ≥ 10

### Performance

* Accuracy: ~72%
* Explainability: SHAP

---

## Project Architecture

Faculty/User

↓

React Frontend

↓

FastAPI Backend

↓

Machine Learning Model (XGBoost)

↓

SHAP Explainability

↓

Intervention Recommendations

↓

PostgreSQL Database

---

## Project Structure

FAILSAFE/

├── backend/

├── frontend/

├── ml-model/

├── dataset/

├── docs/

├── screenshots/

├── requirements.txt

└── README.md

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Poojitharoddam/FAILSAFE.git
cd FAILSAFE
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Backend

Navigate to backend folder:

```bash
cd backend
```

Start FastAPI server:

```bash
uvicorn main:app --reload
```

Backend URL:

```plaintext
http://127.0.0.1:8000
```

API Documentation:

```plaintext
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Navigate to frontend folder:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Start React application:

```bash
npm start
```

Frontend URL:

```plaintext
http://localhost:3000
```

---

## Screenshots

### Dashboard

Interactive student assessment dashboard.

### Prediction Result

Displays risk level and probability.

### SHAP Explainability

Visual explanation of model predictions.

### Accuracy Report

Classification metrics and model performance.

---

## Future Enhancements

* Real-time student monitoring
* Faculty notification system
* Advanced intervention planning
* Cloud deployment
* Multi-institution support
* Deep Learning based prediction models

---

## Conclusion

FAILSAFE demonstrates how Explainable Artificial Intelligence can be applied in education to identify students at risk of failure before academic performance deteriorates significantly.

By combining Machine Learning, Explainable AI, and a modern web application architecture, the system provides actionable insights that help educators support students effectively and improve overall academic outcomes.

---

## Team

Project: FAILSAFE – AI-Powered Student Failure Risk Prediction System

Developed as part of an Academic Mini Project.

---

## License

This project is intended for academic and educational purposes.
