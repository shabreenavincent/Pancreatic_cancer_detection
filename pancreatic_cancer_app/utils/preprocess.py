import cv2
import numpy as np

def preprocess_ct_image(image_array):
    """
    Preprocess CT image for CNN prediction
    """
    image = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (224, 224))  # change only if trained differently
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image
