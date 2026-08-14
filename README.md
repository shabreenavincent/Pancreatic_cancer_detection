# 🩺 Pancreatic Cancer Detection Using Biomarkers and CT Images

An **AI-powered healthcare project** that combines **CT image analysis** and **biomarker-based prediction** to support the **early detection of pancreatic cancer**. The system integrates a **CNN-based CT model** with a **multiclass biomarker prediction model** to generate an integrated diagnostic assessment.

---

## 📌 Project Overview

This project was developed to explore how **Artificial Intelligence, Machine Learning, and Deep Learning** can be applied to a real-world healthcare problem. It uses **two complementary medical data sources**:

* **CT Images** for image-based pancreatic abnormality analysis
* **Biomarker Data** for structured clinical prediction

The outputs from both models are combined to provide a **more comprehensive diagnostic assessment** than relying on a single modality alone.

---

## 🚀 Key Features

* 🧬 **Biomarker-based pancreatic cancer prediction**
* 🖼️ **CT image classification using a CNN model**
* 🤖 **AI/ML and Deep Learning integration**
* 📊 **Multiclass prediction support**
* 📝 **Integrated diagnostic assessment workflow**
* 💻 **Python-based end-to-end prediction pipeline**
* 🎨 Simple user interface with background assets

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

```text
            ┌──────────────────┐
            │  Patient Input   │
            └────────┬─────────┘
                     │
      ┌──────────────┴──────────────┐
      │                             │
      ▼                             ▼
┌───────────────┐         ┌────────────────┐
│ Biomarker Data│         │   CT Image     │
└───────┬───────┘         └───────┬────────┘
        │                           │
        ▼                           ▼
┌───────────────┐         ┌────────────────┐
│ Preprocessing │         │ Image Preprocess│
└───────┬───────┘         └───────┬────────┘
        │                           │
        ▼                           ▼
┌───────────────┐         ┌────────────────┐
│ Biomarker ML  │         │ CNN CT Model   │
│   (.pkl)      │         │    (.h5)       │
└───────┬───────┘         └───────┬────────┘
        │                           │
        └──────────┬────────────────┘
                   ▼
        ┌────────────────────────┐
        │ Integrated Assessment │
        └──────────┬─────────────┘
                   ▼
        ┌────────────────────────┐
        │ Diagnostic Prediction │
        └────────────────────────┘
```

---

## 🧠 Models Used

### 1. CT Image Model

* **File:** `models/ct_cnn_model.h5`
* **Type:** Convolutional Neural Network (CNN)
* **Purpose:** Analyze CT scan images for pancreatic cancer-related abnormalities.

### 2. Biomarker Prediction Model

* **File:** `models/pancreatic_biomarker_multiclass.pkl`
* **Type:** Machine Learning multiclass prediction model
* **Purpose:** Predict pancreatic cancer-related outcomes from biomarker values.

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/pancreatic-cancer-detection.git
cd pancreatic-cancer-detection
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

**Windows**

```bash
venv\\Scripts\\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the application using:

```bash
python app.py
```

The application will load:

* `ct_cnn_model.h5` for CT image analysis
* `pancreatic_biomarker_multiclass.pkl` for biomarker prediction
* preprocessing and prediction utilities from the `utils/` package

---

## 📊 Example Output

The application generates a diagnostic prediction based on the provided biomarker values and/or CT image input.

### Sample Result

```text
Prediction Status : Pancreatic Cancer Detected
Confidence Level  : High
Diagnostic Result : Further clinical evaluation recommended
```

> Replace this section with your actual output screenshot inside a `screenshots/` folder if available.

---

## 📈 Project Highlights

* ✔️ **Multimodal healthcare AI application**
* ✔️ **CNN-based medical image analysis**
* ✔️ **Machine Learning multiclass prediction**
* ✔️ **Integrated biomarker + CT workflow**
* ✔️ **Reusable preprocessing and prediction utilities**
* ✔️ **Professional Python project structure**

---

## 🎯 Use Cases

* Early pancreatic cancer risk assessment
* AI-assisted clinical decision support
* Medical image analysis research
* Biomarker-driven healthcare analytics
* Academic and healthcare AI demonstration projects

---

## 🔒 Important Note

This project is developed for **educational, research, and AI demonstration purposes**. It is intended to support analysis workflows and **must not be used as a substitute for professional medical diagnosis or treatment decisions**.

---

## 📌 Future Improvements

* Improved CT image preprocessing and segmentation
* Explainable AI (XAI) visualizations
* Web-based clinical dashboard
* Cloud deployment support
* Enhanced multimodal fusion strategies
* Larger clinical validation datasets

---

## 👩‍💻 Author

**Shabreena Vincent**
B.Tech Artificial Intelligence and Data Science

---
