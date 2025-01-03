import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';  // You can style the app here
import App from './App';
import { CookiesProvider } from 'react-cookie';

ReactDOM.render(
  <CookiesProvider>
    <App />
  </CookiesProvider>,
  document.getElementById('root')
);
