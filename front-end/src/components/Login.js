import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { useCookies } from 'react-cookie';
import './Login.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [usernameError, setUsernameError] = useState('');
  const [passwordError, setPasswordError] = useState('');
  const navigate = useNavigate();
  const [, setCookie] = useCookies(['accountDetails']);

  // Validate inputs
  const validateInputs = () => {
    let isValid = true;
    setUsernameError('');
    setPasswordError('');

    if (!username.trim()) {
      setUsernameError('Username is required.');
      isValid = false;
    }

    if (!password.trim()) {
      setPasswordError('Password is required.');
      isValid = false;
    } else if (password.length < 6) {
      setPasswordError('Password must be at least 6 characters long.');
      isValid = false;
    }

    return isValid;
  };

  const handleLogin = async () => {

    // Clear previous error states before trying again
    setError(null);               // Clear the overall error message
    setUsernameError('');         // Clear username error
    setPasswordError('');         // Clear password error
    
    if (!validateInputs()) {
      return; // Don't proceed with login if inputs are invalid
    }

    try {
      const response = await axios.post('/auth/login', {
        username,
        password,
      });
      // Set the accountID cookie upon successful login
      setCookie('accountDetails',{'username': username,'accountid':response.data.accountID})
      
      navigate('/'); // Redirect to home page
    } catch (err) {
      setError('Invalid username or password');
    }
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h1 className="h1-login">Login</h1>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className={`input-field ${usernameError ? 'input-error' : ''}`}
        />
        {usernameError && <p className="error-msg">{usernameError}</p>}
        
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className={`input-field ${passwordError ? 'input-error' : ''}`}
        />
        {passwordError && <p className="error-msg">{passwordError}</p>}
        
        <button 
          onClick={handleLogin} 
          className="login-btn" 
          // disabled={!username || !password || usernameError || passwordError}
        >
          Login
        </button>

        
        {error && <p className="error-msg">{error}</p>}
        
        <p className="signup-link">
          Don't have an account? <a href="/signup">Sign Up</a>
        </p>
      </div>
    </div>
  );
};

export default Login;
