# 🧠 CIFAR-10 Image Classification API

## 📌 Overview
This is a Flask-based web API that accepts an image and returns a prediction of its class based on a deep learning model trained on the CIFAR-10 dataset. The model can classify images into one of 10 categories: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, or truck.

## 🔧 Tech Stack
- Python
- Flask
- TensorFlow/Keras
- NumPy
- PIL (Pillow)
- **AWS EC2 (for deployment)**


## 🖼️ CIFAR-10 Class Labels
- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck


##Deployment / Demo Link section:
## 🌐 Deployment
This application is deployed on an **AWS EC2 instance**, allowing real-time image predictions via a RESTful API.

### 🔗 Live API Endpoint
The live API endpoint is hosted at:
http://<your-ec2-public-ip>:7080/predict

## ▶️ How to Run the Project Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/praisy4christ/cifar10-image-classification-api.git
   cd cifar10-image-classification-api
   
## 💡 Highlights
- Built and deployed a deep learning model with TensorFlow
- Developed a REST API using Flask
- Hosted on AWS EC2 for real-time accessibility
  
📦 Install dependencies

pip install -r requirements.txt

🧠 Model
Ensure the trained model file cifar10_model.h5 is in the root directory.

▶️ Running the App Locally
bash
Copy
Edit
python app.py
The API will be available at:
http://localhost:7080/

📡 How to Use the API
Endpoint:
bash
Copy
Edit
POST /predict
Request:
Method: POST

Content-Type: multipart/form-data

Body:

Key: file

Value: Image file (e.g., .jpg, .png)

Example using Postman:
Set method to POST

URL: http://<your-ec2-ip>:7080/predict

Under Body tab, select form-data

Key: file

Type: File

Value: (choose your image file)

Click Send

Sample Response:
json
Copy
Edit
{
  "Predicted Class": "cat",
  "Confidence": 0.9823
}



🧑‍💻 Author
Praisy

GitHub

LinkedIn
