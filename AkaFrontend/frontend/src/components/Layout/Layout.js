// components/Layout.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import HamburgerMenu from '../Menu/Menu';
import './Layout.css';

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <header className="header">
        <div className="container">
          <Link to="/" className="logo">
            <h2>Tournament App</h2>
          </Link>
          <HamburgerMenu />
        </div>
      </header>

      <main className="main-content">
        {children}
      </main>
    </div>
  );
};

export default Layout;