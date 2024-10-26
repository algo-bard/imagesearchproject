from flask import Flask, request, jsonify
import numpy as np
import sqlite3
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load image features from the database
def load_image_features():
    try:
        conn = sqlite3.connect('/Users/arturo/Documents/CodingProjects/IMGTagSearch/image_features.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM image_features')
        rows = cursor.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        raise Exception(f"Database error: {e}")

@app.route('/search_image', methods=['POST'])
def search_image():
    try:
        # Get image features from the request
        search_features = np.array(request.json['features'], dtype=np.float32)
        if search_features.ndim > 2:
            return jsonify({"error": "Invalid input dimension. Expected 1D or 2D array."}), 400

        # Load image features from the database
        rows = load_image_features()

        # Calculate similarities between the input features and database features
        similarities = []
        for row in rows:
            db_features = np.frombuffer(row[1], dtype=np.float32)
            if len(search_features.shape) == 1:
                similarity = cosine_similarity([search_features], [db_features])[0][0]
            else:
                similarity = cosine_similarity(search_features, [db_features])[0][0]
            similarities.append((row[0], similarity))

        # Sort by similarity score (highest first)
        similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:5]

        return jsonify(similarities)

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/search_by_text', methods=['POST'])
def search_by_text():
    try:
        # Get text vector from the request
        query_vector = np.array(request.json['query_vector'], dtype=np.float32)
        if query_vector.ndim != 1:
            return jsonify({"error": "Invalid input dimension for query vector. Expected 1D array."}), 400

        # Load image features from the database
        rows = load_image_features()

        # Calculate similarities between the query vector and image features
        similarities = []
        for row in rows:
            db_features = np.frombuffer(row[1], dtype=np.float32)
            if len(db_features) == len(query_vector):
                similarity = cosine_similarity([query_vector], [db_features])[0][0]
                similarities.append((row[0], similarity))
            else:
                continue

        # Sort by similarity score (highest first)
        similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:5]

        return jsonify(similarities)

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
