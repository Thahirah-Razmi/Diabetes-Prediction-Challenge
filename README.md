# 🩸 Diabetes Prediction Challenge – Kaggle Competition Solution

[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green)](https://flask.palletsprojects.com/)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.5+-red)](https://xgboost.readthedocs.io/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Competition-blue)](https://www.kaggle.com/competitions/playground-series-s5e12)
[![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

**End‑to‑end ML solution** for the Kaggle Playground Series S5E12 – Diabetes Prediction.  
**700k** training records, **300k** test records, 26 features.  
Three models compared: **XGBoost** (best), **Random Forest**, **Artificial Neural Network**.  
The winning XGBoost model is deployed as a **Flask web app** for real‑time diabetes risk prediction.

---

## 📌 Table of Contents
- [Competition Overview](#-competition-overview)
- [EDA Highlights](#-eda-highlights)
- [Models & Hyperparameters](#-models--hyperparameters)
- [Performance Summary](#-performance-summary)
- [Web App](#-web-app)
- [Kaggle Submissions](#-kaggle-submissions)
- [Project Structure](#-project-structure)
- [Installation & Usage](#-installation--usage)
- [Author](#-author)

---

## 🏆 Competition Overview

- **Goal** – Predict diabetes (binary) from diagnostic health metrics  
- **Metric** – ROC AUC  
- **Data** – Synthetic dataset derived from the Pima Indians Diabetes dataset  

🔗 [Competition link](https://www.kaggle.com/competitions/playground-series-s5e12)

---

## 📊 EDA Highlights

Performed comprehensive exploratory data analysis using `pandas`, `matplotlib`, and `seaborn`:

| Visualisation | Insight |
|---------------|---------|
| **Target distribution** (bar & pie) | ~62% diabetic, ~38% non‑diabetic |
| **Histograms of all numeric features** | Glucose, BMI, Age show right‑skewed distributions |
| **Boxplots by diabetes outcome** | Higher BMI, more belly fat (waist-to-hip ratio), higher bad cholesterol (LDL), higher triglycerides, and higher blood pressure (systolic_bp and diastolic_bp) for diabetic patients. They also exercise slightly less. |
| **Count plots for categorical variables** | Gender, smoking status, education, income, employment, ethnicity – clear differences in diabetes prevalence |
| **Correlation heatmap** | cholesterol_total & ldl_cholesterol (0.81),	bmi & waist_to_hip_ratio (0.76) and	age and systolic_bp (0.50) strongest positive correlations with diabetes |

All EDA plots are included in the `/images` folder.

---

## 🧠 Models & Hyperparameters

| Model | Key Hyperparameters |
|-------|----------------------|
| **Random Forest** | n_estimators=400, max_depth=18, min_samples_leaf=30, class_weight='balanced' |
| **XGBoost** | n_estimators=800, max_depth=8, learning_rate=0.05, scale_pos_weight=scale_pos_weight |
| **ANN** | 3 Dense Layers (128, 641, 1) with Dropout(0.3 & 0.2), Adam optimizer, class_weight='balanced' |

All models use a `ColumnTransformer` with `StandardScaler` for numeric features and `OneHotEncoder` for categorical ones.

---

## 📈 Performance Summary (Training set)

| Model | ROC AUC | Accuracy |
|-------|---------|----------|
| Random Forest | 0.7666 | 0.6843 |
| **XGBoost** | **0.7946** | **0.7075** |
| ANN | 0.7069 | 0.6335 |

**XGBoost** selected as the final production model.  
Confusion matrices and ROC curves for all three models are saved in `/images`.

---

## 🌐 Web Application

Built with **Flask** – loads the trained XGBoost pipeline (`diapredict_model.pkl` + `preprocessor.pkl`).

- **Inputs**: Age, alcohol consumption, diet score, sleep, screen time, BMI, waist‑to‑hip ratio, blood pressure, heart rate, cholesterol (total/HDL/LDL), triglycerides, family history, hypertension, cardiovascular history, gender, ethnicity, education, income, smoking, employment.
- **Output**: Diabetes risk (Diabetic / Non‑Diabetic) + probability percentage.
- **Responsive UI** with risk meter and health message.

### 🚀 Installation

<summary><strong>1. Clone Repository</strong></summary>
  
```
git clone https://github.com/Thahirah-Razmi/Diabetes-Prediction-Kaggle-Challenge.git
cd Diabetes-Prediction-Kaggle-Challenge
```

<summary><strong>2. Create Virtual Environment (Recommended)</strong></summary>
  
```bash
# Create virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

<summary><strong>3. Install Dependencies</strong></summary>
  
```
pip install -r requirements.txt
```
Or install packages individually:

```bash
pip install flask numpy pandas scikit-learn xgboost tensorflow matplotlib seaborn joblib
```

## 🏃 Running the Application

```bash
python DiaPredict.py
```
The application will run at ``` http://127.0.0.1:5000 ```

## 📸 Visual Previews  
### DiaPredict's UI

<img width="1004" height="1195" alt="image" src="https://github.com/user-attachments/assets/ee14516a-7a95-4944-aea3-9875b1399906" />



## 📊 Kaggle Submissions

<img width="1920" height="1019" alt="Kaggle Submission" src="https://github.com/user-attachments/assets/b5f9bad0-513f-4cc4-833b-b3b58e308958" />

## 👩‍💻 Author  

[Thahirah Razmi](https://github.com/Thahirah-Razmi)
