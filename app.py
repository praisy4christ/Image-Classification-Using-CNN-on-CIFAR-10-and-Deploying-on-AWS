
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Load trained model
model = tf.keras.models.load_model("cifar10_model.h5")

# CIFAR-10 class names
class_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the CIFAR-10 Image Classification API!"

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    img = Image.open(io.BytesIO(file.read())).resize((32, 32))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 32, 32, 3)

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    return jsonify({"Predicted Class": predicted_class, "Confidence": confidence})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7080)
