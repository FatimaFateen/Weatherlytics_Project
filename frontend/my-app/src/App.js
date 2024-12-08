// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import WeatherForm from './components/WeatherForm';

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login/>} />
          
 
          <Route path="/predict" element={<WeatherForm />} />
         
          {/* You can add more routes here as needed */}
        </Routes>
      </div>
    </Router>
  );
};

export default App;
