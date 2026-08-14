# 🩺 A Hybrid Radiomics–Biomarker Framework for Pancreatic Cancer Risk Prediction

An **AI-powered healthcare screening system** that combines **biomarker-based risk assessment** with **CNN-based CT scan confirmation** for pancreatic cancer detection. The application follows a **two-stage hybrid workflow** that performs biomarker screening first and triggers CT analysis only for patients identified as **high risk**, making the screening process more efficient and clinically meaningful.

---

## 📌 Project Overview

This project was developed to explore how **Artificial Intelligence, Machine Learning, Deep Learning, and medical image analysis** can be applied to a real-world healthcare problem. The system integrates **structured biomarker data** with **radiological CT imaging** to support **early pancreatic cancer risk prediction and confirmation**.

### Biomarker Inputs

* Age
* Sex
* Creatinine
* Plasma CA19-9
* TFF1
* REG1B
* REG1A
* LYVE1

The biomarker values are analyzed using a **multiclass machine-learning model** (`pancreatic_biomarker_multiclass.pkl`). Depending on the prediction, the patient is classified as **Healthy**, **Likely Benign**, or **High Cancer Risk**. Only high-risk patients are directed to the **CT Scan Confirmation module**, where a **CNN-based deep-learning model** (`ct_cnn_model.h5`) analyzes the uploaded abdominal CT scan. The final diagnosis combines the biomarker screening outcome with the CT confirmation result to generate an **integrated diagnostic assessment and clinical recommendation**.

---

## 🚀 Key Features

* **Two-stage hybrid screening workflow**
* **Biomarker-based multiclass risk prediction**
* **Age and sex aware patient assessment**
* **Clinical biomarker analysis (CA19-9, TFF1, REG1B, REG1A, LYVE1, Creatinine)**
* **Automated Healthy / Benign / High-Risk classification**
* **Conditional CT scan confirmation for high-risk patients**
* **CNN-based abdominal CT image analysis**
* **Integrated final diagnostic assessment**
* **Clinical recommendation generation**
* **Interactive healthcare-focused user interface**

---

## 🛠️ Technology Stack

| Category                | Technology         |
| ----------------------- | ------------------ |
| Programming Language    | Python             |
| Artificial Intelligence | AI                 |
| Machine Learning        | Scikit-learn       |
| Deep Learning           | TensorFlow / Keras |
| Neural Networks         | CNN                |
| Model Serialization     | Pickle (.pkl)      |
| Image Processing        | OpenCV / PIL       |
| Development Environment | VS Code            |
| Version Control         | Git & GitHub       |

---

## 📂 Project Structure

```text
pancreatic_cancer_app/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── background.jpg
│
├── models/
│   ├── ct_cnn_model.h5
│   └── pancreatic_biomarker_multiclass.pkl
│
├── utils/
│   ├── preprocess.py
│   └── predict.py
│
└── venv/
```

---

## 🔄 System Workflow

The application follows a **sequential hybrid screening process** designed to minimize unnecessary CT analysis and mimic a realistic clinical decision workflow.

### Workflow Diagram

```text
        Patient Details + Biomarkers
                     │
                     ▼
        ┌────────────────────────────┐
        │ Biomarker ML Screening    │
        │ (.pkl multiclass model)   │
        └─────────────┬──────────────┘
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
 ┌──────────┐ ┌────────────────┐ ┌────────────────────┐
 │ Healthy  │ │ Likely Benign │ │ High Cancer Risk  │
 └──────────┘ └────────────────┘ └──────────┬─────────┘
                                               │
                                               ▼
                              ┌────────────────────────┐
                              │ CT Scan Confirmation   │
                              │ Upload Abdominal CT    │
                              └──────────┬─────────────┘
                                         │
                                         ▼
                              ┌────────────────────────┐
                              │ CNN CT Analysis        │
                              │ (ct_cnn_model.h5)      │
                              └──────────┬─────────────┘
                                         │
                                         ▼
                              ┌────────────────────────┐
                              │ Final Diagnostic       │
                              │ Assessment             │
                              └────────────────────────┘
```

---

## 🧠 How the Application Works

### Step 1 – Patient Screening

The user enters demographic details and biomarker values through the screening interface.

### Step 2 – Biomarker Risk Assessment

The biomarker model evaluates the input values and predicts one of three categories:

* **Healthy**
* **Likely Benign Condition**
* **High Cancer Risk Detected**

### Step 3 – Conditional CT Analysis

If the patient is classified as **High Cancer Risk**, the application activates the **CT Scan Confirmation module** and requests an abdominal CT scan upload.

### Step 4 – CT Confirmation

The uploaded CT image is processed and analyzed using the **CNN-based deep-learning model** to identify imaging patterns associated with pancreatic cancer.

### Step 5 – Final Diagnosis

The CT confirmation result is combined with the biomarker screening outcome to generate the **final diagnostic assessment and clinical recommendation**.

---

## 🧠 Models Used

### 1. Biomarker Prediction Model

* **File:** `models/pancreatic_biomarker_multiclass.pkl`
* **Purpose:** Predict pancreatic cancer risk from biomarker values.
* **Output Classes:** Healthy, Likely Benign, High Cancer Risk.

### 2. CT Image Confirmation Model

* **File:** `models/ct_cnn_model.h5`
* **Purpose:** Analyze abdominal CT scans for pancreatic cancer-related abnormalities.
* **Type:** Convolutional Neural Network (CNN).

---

## 📊 Example Results

### ✅ Healthy Screening Result

* **Result:** Healthy
* **Recommendation:** Balanced diet, regular exercise, annual health check-up.

### ⚠️ Likely Benign Condition

* **Result:** Likely Benign Condition
* **Recommendation:** Gastroenterology consultation, possible ultrasound evaluation, dietary management.

### 🚨 High Cancer Risk Detected

* **Result:** High Cancer Risk Detected
* **Recommendation:** Proceed to CT Scan Confirmation.

### 🩻 CT Scan Confirmation

* Upload abdominal CT image
* CNN-based CT analysis is performed automatically

### 🧾 Final Diagnosis

**Example Output:**

```text
Final Diagnosis: Pancreatic Cancer Detected

Immediate Recommendations:
- Consult an oncologist immediately
- Further imaging (MRI / biopsy)
- Multidisciplinary cancer care evaluation
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/shabreenavincent/Pancreatic_cancer_detection.git
cd pancreatic-cancer-detection
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

**Windows**

```bash
venv\\Scripts\\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the application using:

```bash
python app.py
```

The application automatically loads:

* `pancreatic_biomarker_multiclass.pkl` for biomarker screening
* `ct_cnn_model.h5` for CT scan confirmation
* preprocessing and prediction utilities from the `utils/` package

---

## 📈 Project Highlights

* ✔️ **Sequential hybrid screening architecture**
* ✔️ **Biomarker-driven primary risk assessment**
* ✔️ **Conditional CNN-based CT confirmation**
* ✔️ **Integrated diagnostic decision workflow**
* ✔️ **Clinical recommendation generation**
* ✔️ **Professional Python project organization**
* ✔️ **Healthcare-oriented interactive user interface**

---

## 🎯 Use Cases

* Early pancreatic cancer risk screening
* AI-assisted clinical decision support
* Biomarker-driven healthcare analytics
* Medical image analysis research
* Academic and healthcare AI demonstration projects
* Hybrid radiomics and biomarker research workflows

---

## 🔒 Important Note

This project is intended for **educational, research, and AI demonstration purposes only**. It is designed to support screening and analysis workflows and **must not be used as a substitute for professional medical diagnosis or treatment decisions**.

---

## 🔮 Future Enhancements

* Advanced CT image segmentation
* Explainable AI (XAI) visualizations
* Probability-based risk scoring
* PDF diagnostic report export
* Web-based clinical dashboard
* Cloud deployment support
* Larger clinical validation datasets
* Improved multimodal fusion strategies

---

## 👩‍💻 Author

**Shabreena Vincent**
B.Tech Artificial Intelligence and Data Science

---
