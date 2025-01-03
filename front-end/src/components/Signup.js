import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Signup.css';

const Signup = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [usernameError, setUsernameError] = useState('');
  const [emailError, setEmailError] = useState('');
  const [passwordError, setPasswordError] = useState('');
  const navigate = useNavigate();

  const validateForm = () => {
    let valid = true;

    // Reset errors
    setUsernameError('');
    setEmailError('');
    setPasswordError('');

    if (!username) {
      setUsernameError('Username is required');
      valid = false;
    }

    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (!email || !emailPattern.test(email)) {
      setEmailError('Enter a valid email');
      valid = false;
    }

    if (!password || password.length < 6) {
      setPasswordError('Password must be at least 6 characters');
      valid = false;
    }

    return valid;
  };

  const handleSignup = async () => {

    // Clear previous error states before trying again
    setError(null);
    setUsernameError('');
    setEmailError('');
    setPasswordError('');

    if (validateForm()) {
      try {
        const response = await axios.post('/auth/signup', {
          username,
          email,
          password,
        });

        // Redirect to login page upon successful signup
        navigate('/login');
      } catch (err) {
        setError(err.response ? err.response.data.message : 'Signup failed');
      }
    }
  };

  // Update email error when the user changes the email field
  const handleEmailChange = (e) => {
    setEmail(e.target.value);
    if (emailError) {
      setEmailError(''); // Clear error message when user starts typing
    }
  };

  return (
    <div className="signup-container">
      <div className="signup-box">
        <h1 className="h1-signup">Sign Up</h1>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className={`input-field ${usernameError ? 'input-error' : ''}`}
        />
        {usernameError && <p className="error-msg">{usernameError}</p>}
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={handleEmailChange}  
          className={`input-field ${emailError ? 'input-error' : ''}`}
        />
        {emailError && <p className="error-msg">{emailError}</p>}
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className={`input-field ${passwordError ? 'input-error' : ''}`}
        />
        {passwordError && <p className="error-msg">{passwordError}</p>}
        <button
          onClick={handleSignup}
          className="signup-btn"
          // disabled={!username || !email || !password || usernameError || emailError || passwordError}
        >
          Sign Up
        </button>
        {error && <p className="error-msg">{error}</p>}
        <p className="login-link">
          Already have an account? <a href="/login">Login</a>
        </p>
      </div>
    </div>
  );
};

export default Signup;
