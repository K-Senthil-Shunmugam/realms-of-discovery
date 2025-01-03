import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Home from './components/Home';
import Login from './components/Login';
import Signup from './components/Signup';
import Play from './components/Play'; // import the Play component
import { useCookies } from 'react-cookie';

function App() {
  const [cookies] = useCookies(['accountDetails']); // Check if user is logged in
  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={cookies.accountDetails=== undefined || cookies.accountDetails === 'undefined' ? <Navigate to="/login" /> : <Home />}
        />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/play" element={<Play />} />
      </Routes>
    </Router>
  );
}

export default App;

