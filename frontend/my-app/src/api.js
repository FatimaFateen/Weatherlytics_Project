// src/api.js
import axios from 'axios';

const API_URL = 'http://localhost:5001'; // Backend URL
//const API_URL = process.env.REACT_APP_BACKEND_URL
console.log("API URL:", API_URL);



export const signup = async (Mlops_project) => {
  try {
    const response = await axios.post(`${API_URL}/signup`, Mlops_project);
    return response.data; // Return the response data if needed
  } catch (error) {
    console.error('Signup API error:', error);
    console.error('Error Config:', error.config);
    console.error('Error Request:', error.request);
    if (error.response) {
        console.error('Error Response:', error.response.data);
    } else {
        console.error('No Response Received:', error.message);
    }
    throw error.response ? error.response.data : new Error('Network error');}
  };


export const login = async (Mlops_project) => {
  try {
    const response = await axios.post(`${API_URL}/login`, Mlops_project);
    return response.data; // Return the response data if needed
  } catch (error) {
    console.error('Login API error:', error);
    throw error.response ? error.response.data : new Error('Network error');
  }
};

 // Predict weather using trained model
export const predictWeather = async (humidity, windSpeed) => {
    try {
      // Send the weather data to the backend without Authorization header
      const response = await axios.post(`${API_URL}/predict`, {
        humidity,
        windSpeed
      });
  
      return response.data; // Return the prediction result from the backend
    } catch (error) {
      console.error('Weather Prediction API error:', error);
      throw error.response ? error.response.data : new Error('Network error');
    }
  }; 
  

export const forgotPassword = async (email) => {
  try {
    const response = await axios.post(`${API_URL}/forgot-password`, { email });
    return response.data; // Return the response data if needed
  } catch (error) {
    // Enhanced error handling
    console.error('Forgot Password API error:', error.response ? error.response.data : error.message);
    throw error.response ? error.response.data : new Error('Network error');
  }
};

export const resetPassword = async (token, newPassword) => {
  try {
    const response = await axios.post(`${API_URL}/reset-password`, { token, new_password: newPassword });
    return response.data; // Return the response data if needed
  } catch (error) {
    console.error('Reset Password API error:', error);
    throw error.response ? error.response.data : new Error('Network error');
  }
};
