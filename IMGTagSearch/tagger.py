from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, decode_predictions, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import sqlite3
import os
import spacy

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

# Load spaCy model for text processing
nlp = spacy.load('en_core_web_md')

# Ensure the database exists and create a table for image features
db_path = 'feature_database.db'
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE image_features (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        features BLOB,
        relevance_score INTEGER DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

def tag_image(image_path):
    # Load the image and preprocess it
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    # Extract features using the model
    features = model.predict(image)

    # Store the features in the database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('INSERT INTO image_features (filename, features) VALUES (?, ?)', (os.path.basename(image_path), features.tobytes()))
    conn.commit()
    conn.close()

    return features

def text_to_vector(text):
    doc = nlp(text)
    return doc.vector
