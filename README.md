# 🩸 Diabetes Prediction Challenge - Kaggle Competition Solution

[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.5+-red)](https://xgboost.readthedocs.io/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-yellow)](https://tensorflow.org/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Competition-blue)](https://www.kaggle.com/competitions/playground-series-s5e12)
[![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

A complete machine learning solution for the **Kaggle Playground Series Season 5 Episode 12 - Diabetes Prediction Challenge**. This project implements and compares multiple ML algorithms including **Artificial Neural Networks (ANN)**, **XGBoost**, and **Random Forest** to predict diabetes onset. The best-performing model (XGBoost) is deployed as a production-ready **Flask web application** with a user-friendly interface.

---

## 📌 Table of Contents
- [Competition Overview](#-competition-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Models Implemented](#-models-implemented)
- [Getting Started](#-getting-started-installation)
- [Web Application](#-web-application)
- [Kaggle Submissions](#-kaggle-submissions)
- [Model Performance](#-model-performance)
- [Project Structure](#-project-structure)
- [Visual Previews](#-visual-previews)
- [Author](#-author)
- [License](#-license)

---

## 🏆 Competition Overview

**Playground Series Season 5 Episode 12 - Diabetes Prediction Challenge**

This Kaggle competition focuses on predicting diabetes onset using diagnostic health metrics. The dataset contains medical predictor variables and a binary target variable indicating diabetes presence. This is a binary classification problem where models predict whether a patient has diabetes based on features like glucose level, BMI, age, blood pressure, insulin, etc.

- **Goal**: Predict diabetes status (1 = diabetic, 0 = non-diabetic)
- **Evaluation Metric**: ROC AUC Score
- **Data Source**: Synthetic dataset derived from the original Diabetes dataset

🔗 [Competition Link](https://www.kaggle.com/competitions/playground-series-s5e12)

---

## ✨ Features

### Data Processing & Analysis
- **Exploratory Data Analysis (EDA)** - Comprehensive data visualization and statistical analysis
- **Missing Value Handling** - Advanced imputation strategies
- **Feature Engineering** - Creating meaningful features from existing data
- **Data Normalization** - StandardScaler for feature scaling

### Machine Learning Models
- **Artificial Neural Network (ANN)** - Deep learning approach with multiple hidden layers
- **XGBoost Classifier** - Gradient boosting with regularization (Best performing)
- **Random Forest Classifier** - Ensemble learning with bootstrap aggregation
- **Model Comparison** - Performance evaluation across all models

### Web Application
- **Flask Web Interface** - Clean, responsive UI for real-time predictions
- **Form Input Validation** - Sanitizes and validates all health metrics
- **Instant Predictions** - Real-time diabetes risk assessment
- **Model Selection** - Choose which model to use for prediction
- **Probability Output** - Get prediction confidence scores

### Kaggle Integration
- **Competition Submission** - Generate submission files for Kaggle leaderboard
- **Public & Private Leaderboard** - Validated submissions
- **Cross-Validation** - Robust model validation strategy

---

## 💻 Tech Stack

| Category           | Technology                                      |
| ------------------ | ----------------------------------------------- |
| **Languages**      | Python 3.9+                                     |
| **Web Framework**  | Flask 2.0+                                      |
| **ML Framework**   | scikit-learn, XGBoost, TensorFlow/Keras         |
| **Data Processing**| Pandas, NumPy                                   |
| **Visualization**  | Matplotlib, Seaborn                             |
| **Model Persistence** | joblib, pickle                               |
| **Frontend**       | HTML5, CSS3, Bootstrap 5                        |
| **Deployment**     | Local Server / Cloud Ready                      |

---

## 🧠 Models Implemented

| Model | Type | Key Features | Hyperparameters |
|-------|------|--------------|-----------------|
| **Random Forest** | Ensemble (Bagging) | 400 trees, balanced class weight | n_estimators=400, max_depth=18, min_samples_leaf=30 |
| **XGBoost** | Ensemble (Boosting) | Gradient boosting with scale_pos_weight | n_estimators=800, max_depth=8, learning_rate=0.05 |
| **ANN** | Deep Neural Network | 2 hidden layers (128, 64) with Dropout | ReLU activation, Adam optimizer, class_weight='balanced' |

### Model Architecture (ANN)
