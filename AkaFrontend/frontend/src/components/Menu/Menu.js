// components/HamburgerMenu.jsx
import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FaBars, FaTimes } from 'react-icons/fa';
import './Menu.css';

const MenuIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
    <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/>
  </svg>
);

const CloseIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
    <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
  </svg>
);

const HamburgerMenu = () => {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();

  //console("CWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEL")
  // Close menu when route changes
  useEffect(() => {
    setIsOpen(false);
  }, [location]);

  // Close menu when clicking on a link
  const handleLinkClick = () => {
    setIsOpen(false);
  };

  // Close menu when clicking outside or pressing escape
  useEffect(() => {
    const handleClickOutside = (event) => {
      const menu = document.querySelector('.menu-content');
      const hamburger = document.querySelector('.hamburger-btn');
      
      if (isOpen && menu && !menu.contains(event.target) && 
          hamburger && !hamburger.contains(event.target)) {
        setIsOpen(false);
      }
    };

    const handleEscapeKey = (event) => {
      if (event.key === 'Escape') {
        setIsOpen(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    document.addEventListener('keydown', handleEscapeKey);

    // Disable body scroll when menu is open on mobile
    if (!isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }

    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
      document.removeEventListener('keydown', handleEscapeKey);
      document.body.style.overflow = 'unset';
    };
  }, [isOpen]);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="hamburger-menu">
      {/* Hamburger Button */}
      <button 
        className="hamburger-btn" 
        onClick={toggleMenu}
        aria-label="Toggle menu"
        aria-expanded={isOpen}
      >
        {isOpen ? <CloseIcon /> : <MenuIcon />}
      </button>

      {/* Menu Overlay */}
      <div className={`menu-overlay ${isOpen ? 'active' : ''}`} onClick={toggleMenu}></div>

      {/* Menu Content */}
      <div className={`menu-content ${isOpen ? 'active' : ''}`}>
        <ul className="menu-list">
          <li>
            <Link to="/" onClick={handleLinkClick}>Główna strona</Link>
          </li>
          <li>
            <Link to="/brackets" onClick={handleLinkClick}>Drabinki kumite</Link>
          </li>
          <li>
            <Link to="/dojolist" onClick={handleLinkClick}>Dojo</Link>
          </li>
          {/* Add more navigation items as needed */}
        </ul>
      </div>
    </nav>
  );
};

export default HamburgerMenu;