import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "pancreatic_biomarker_multiclass.pkl"
)

biomarker_model = joblib.load(MODEL_PATH)

def biomarker_predict(input_df):
    # Ensure correct feature order
    expected_features = biomarker_model.feature_names_in_
    input_df = input_df[expected_features]

    prediction = biomarker_model.predict(input_df)[0]
    probabilities = biomarker_model.predict_proba(input_df)[0]

    return prediction, probabilities


import tensorflow as tf
from utils.preprocess import preprocess_ct_image

CT_MODEL_PATH = os.path.join(BASE_DIR, "models", "ct_cnn_model.h5")

ct_model = tf.keras.models.load_model(CT_MODEL_PATH)

def ct_predict(image_array):
    processed = preprocess_ct_image(image_array)
    prediction = ct_model.predict(processed)[0][0]
    return prediction
