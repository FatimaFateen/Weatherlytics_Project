// src/components/Signup.js
import React, { useState } from 'react';
import { signup } from '../api';

const Signup = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(''); // State for success message

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await signup({ email, password });
      setSuccess('Signup successful! You can now log in.'); // Set success message
      setError(''); // Clear any previous error messages
      // Optionally, you can redirect to the login page or reset the form
      setEmail('');
      setPassword('');
    } catch (err) {
      setError(err.message || 'Signup failed'); // Display the error message
      setSuccess(''); // Clear any previous success messages
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Signup</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>} {/* Error message styling */}
      {success && <p style={{ color: 'green' }}>{success}</p>} {/* Success message styling */}
      <input
        type="text"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <button type="submit">Signup</button>
    </form>
  );
};

export default Signup;
