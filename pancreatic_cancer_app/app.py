import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import base64
import os

def set_background():
    image_path = os.path.join("assets", "background.jpg")  # 👈 image name here

    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


from utils.predict import biomarker_predict, ct_predict

# --------------------------------------------------
# Page setup
# --------------------------------------------------
st.set_page_config(
    page_title="Pancreatic Cancer Detection System",
    page_icon="🧬",
    layout="centered"
)
set_background()

if "page" not in st.session_state:
    st.session_state.page = "input"

# --------------------------------------------------
# PAGE 1: Biomarker Input
# --------------------------------------------------
def page_input():
    # Centered heading
    st.markdown(
        "<h1 style='text-align: center;'>🧬A Hybrid Radiomics–Biomarker Framework for Pancreatic Cancer Risk Prediction</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
    """
    <p style="
        text-align: center;
        font-size: 16px;
        font-weight: 500;
        margin-bottom: 25px;
        color: #e0e0e0;
    ">
        Enter patient details and biomarkers
    </p>
    """,
    unsafe_allow_html=True
)


    st.write("")  # spacing

    # -------- Row 1: Age & Sex --------
    col_age, col_sex = st.columns(2)

    with col_age:
        age = st.number_input("Age", 30, 90, step=1)

    with col_sex:
        sex = st.radio("Sex", ["Female", "Male"], horizontal=True)
        sex_M = 1 if sex == "Male" else 0

    st.write("")  # spacing

    # -------- Row 2–4: Biomarkers (3x2 grid) --------
    col1, col2 = st.columns(2)
    with col1:
        creatinine = st.number_input("Creatinine", min_value=0.0, format="%.5f")
    with col2:
        plasma_ca19 = st.number_input("Plasma CA19-9", min_value=0.0, format="%.5f")

    col3, col4 = st.columns(2)
    with col3:
        tff1 = st.number_input("TFF1", min_value=0.0, format="%.5f")
    with col4:
        reg1b = st.number_input("REG1B", min_value=0.0, format="%.5f")

    col5, col6 = st.columns(2)
    with col5:
        reg1a = st.number_input("REG1A", min_value=0.0, format="%.5f")
    with col6:
        lyve1 = st.number_input("LYVE1", min_value=0.0, format="%.5f")

    st.write("")  # spacing

    # -------- Run Button --------
    if st.button("Run Biomarker Screening"):
        input_df = pd.DataFrame([{
            "LYVE1": lyve1,
            "REG1A": reg1a,
            "REG1B": reg1b,
            "TFF1": tff1,
            "plasma_CA19_9": plasma_ca19,
            "creatinine": creatinine,
            "age": age,
            "sex_M": sex_M
        }])

        pred, probs = biomarker_predict(input_df)

        st.session_state.prediction = pred
        st.session_state.probabilities = probs
        st.session_state.page = "result"
        st.rerun()


# --------------------------------------------------
# PAGE 2: Biomarker Result
# --------------------------------------------------
def page_result():
    st.title("🧪 Biomarker Screening Result")

    pred = st.session_state.prediction
    probs = st.session_state.probabilities

    if pred == 0:
        st.success("🟢 Result: Healthy")
        st.write("### Recommended Actions")
        st.markdown("""
        - Maintain a balanced diet  
        - Regular exercise / yoga  
        - Annual health check-up  
        """)

    elif pred == 1:
        st.warning("🟡 Result: Likely Benign Condition")
        st.write("### Clinical Advice")
        st.markdown("""
        - Possible gallstones or benign abdominal condition  
        - Consult a gastroenterologist  
        - Ultrasound may be recommended  
        - Dietary fat control  
        """)

    else:
        st.error("🔴 Result: High Cancer Risk Detected")
        st.write("Further imaging is recommended.")
        if st.button("Proceed to CT Scan Confirmation"):
            st.session_state.page = "ct"
            st.rerun()

    if st.button("Start New Screening"):
        st.session_state.clear()
        st.session_state.page = "input"
        st.rerun()

# --------------------------------------------------
# PAGE 3: CT Scan Upload
# --------------------------------------------------
def page_ct():
    st.title("🩻 CT Scan Confirmation")

    uploaded = st.file_uploader(
        "Upload Abdominal CT Scan",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        st.image(image, caption="Uploaded CT Scan", width=300)

        if st.button("Analyze CT Scan"):
            score = ct_predict(np.array(image))
            st.session_state.ct_score = score
            st.session_state.page = "final"
            st.rerun()

# --------------------------------------------------
# PAGE 4: Final Diagnosis
# --------------------------------------------------
def page_final():
    st.title("📋 Final Diagnosis")

    score = st.session_state.ct_score

    if score > 0.5:
        st.error("🔴 Pancreatic Cancer Detected")
        st.markdown("""
        ### Immediate Recommendations
        - Consult an oncologist immediately  
        - Further imaging (MRI / biopsy)  
        - Multidisciplinary cancer care  
        """)
    else:
        st.success("🟢 No Malignancy Detected on CT")
        st.markdown("""
        ### Next Steps
        - Continue monitoring  
        - Manage benign condition  
        - Follow clinician guidance  
        """)

    if st.button("New Patient"):
        st.session_state.clear()
        st.session_state.page = "input"
        st.rerun()

# --------------------------------------------------
# Page Router
# --------------------------------------------------
if st.session_state.page == "input":
    page_input()
elif st.session_state.page == "result":
    page_result()
elif st.session_state.page == "ct":
    page_ct()
elif st.session_state.page == "final":
    page_final()
