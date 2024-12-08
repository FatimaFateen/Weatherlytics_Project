from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import joblib
import pandas as pd
from pymongo import MongoClient
from flask_jwt_extended import JWTManager, create_access_token
from dotenv import load_dotenv
import os
import logging


load_dotenv()

app = Flask(__name__)

# Apply CORS globally, allowing all origins (you can limit it to specific origins if needed)
 # This applies CORS globally to all routes
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


# Configure JWT secret key
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'MySecretKey')

# Initialize JWT Manager
jwt = JWTManager(app)

# Load the trained model
model = joblib.load('model.pkl') 

# Configure MongoDB
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['Mlops_project']

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)



@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400

    # Check if email already exists
    existing_user = db.users.find_one({'email': email})
    if existing_user:
        return jsonify({"message": "User already exists"}), 400

    # Insert new user into the database
    try:
        db.users.insert_one({
            "email": email,
            "password": password  # Make sure to hash passwords in a real application
        })
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"message": "An error occurred while creating user"}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'msg': 'email and password are required'}), 400

    # Fetch user from the database
    user = db.users.find_one({'email': email})

    # Check if user exists and password is correct
    if user and user['password'] == password:
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'msg': 'Invalid email or password'}), 401

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    humidity = data['humidity']
    wind_speed = data['windSpeed']
    
    # Prepare input for prediction
    input_data = pd.DataFrame([[humidity, wind_speed]], columns=['Humidity', 'Wind Speed'])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    return jsonify({'prediction': prediction})

@app.before_request
def log_request():
    app.logger.debug(f"Incoming request: {request.method} {request.url}")
    app.logger.debug(f"Headers: {request.headers}")
    app.logger.debug(f"Body: {request.get_data()}")


if __name__ == '__main__':
    app.run(debug=True,port=5001)
