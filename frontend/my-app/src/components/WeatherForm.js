import React, { useState } from 'react';

const WeatherForm = () => {
  const [humidity, setHumidity] = useState('');
  const [windSpeed, setWindSpeed] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5001/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          humidity,
          windSpeed,
        }),
      });
      const data = await response.json();
      setPrediction(data.prediction);
    } catch (error) {
      console.error('Error fetching prediction:', error);
    }
  };

  return (
    <div>
      <h2>Weather Prediction</h2>
      <form onSubmit={handleSubmit}>
        <label>Humidity: </label>
        <input
          type="number"
          value={humidity}
          onChange={(e) => setHumidity(e.target.value)}
        />
        <label>Wind Speed: </label>
        <input
          type="number"
          value={windSpeed}
          onChange={(e) => setWindSpeed(e.target.value)}
        />
        <button type="submit">Get Prediction</button>
      </form>
      {prediction && <p>Predicted Temperature: {prediction}°C</p>}
    </div>
  );
};

export default WeatherForm;





